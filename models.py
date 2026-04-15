import os
import sqlite3
from datetime import datetime, timedelta, timezone
from config import Config

# --------------- DB backend detection ---------------

def _use_pg():
    return bool(Config.DATABASE_URL)


def get_db():
    """Return a connection. PostgreSQL when DATABASE_URL set, else SQLite."""
    if _use_pg():
        import psycopg2
        import psycopg2.extras
        url = Config.DATABASE_URL
        # Railway injects postgres:// but psycopg2 needs postgresql://
        if url.startswith("postgres://"):
            url = "postgresql://" + url[len("postgres://"):]
        conn = psycopg2.connect(url, cursor_factory=psycopg2.extras.RealDictCursor)
        conn.autocommit = False
        return conn
    else:
        conn = sqlite3.connect(Config.DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA foreign_keys=ON")
        return conn


def _exec(conn, sql, params=()):
    """Execute a statement, adapting placeholders for the active backend."""
    if _use_pg():
        sql = sql.replace("?", "%s")
    cur = conn.cursor()
    cur.execute(sql, params)
    return cur


def init_db(_db_path=None):
    """Initialize database tables (idempotent)."""
    conn = get_db()
    cur = conn.cursor()

    if _use_pg():
        statements = [
            """
            CREATE TABLE IF NOT EXISTS subscriptions (
                id          SERIAL PRIMARY KEY,
                email       TEXT    NOT NULL,
                threshold   REAL    NOT NULL DEFAULT 0.10,
                currency    INTEGER NOT NULL DEFAULT 29,
                country     TEXT    NOT NULL DEFAULT 'HK',
                created_at  TEXT    NOT NULL,
                expires_at  TEXT    NOT NULL,
                active      INTEGER NOT NULL DEFAULT 1,
                unsub_token TEXT    NOT NULL UNIQUE,
                language    TEXT    NOT NULL DEFAULT 'zh-TW'
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS items (
                id              SERIAL PRIMARY KEY,
                subscription_id INTEGER NOT NULL,
                record_index    INTEGER,
                credit          INTEGER NOT NULL,
                transaction_id  TEXT,
                appid           INTEGER NOT NULL,
                item_name       TEXT    NOT NULL,
                price           REAL    NOT NULL,
                listed_date     TEXT,
                action_date     TEXT,
                quantity        INTEGER NOT NULL DEFAULT 1,
                FOREIGN KEY (subscription_id) REFERENCES subscriptions(id) ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS price_cache (
                item_hash   TEXT    NOT NULL,
                appid       INTEGER NOT NULL,
                lowest      REAL,
                median      REAL,
                volume      TEXT,
                fetched_at  TEXT    NOT NULL,
                PRIMARY KEY (item_hash, appid)
            )
            """,
            "CREATE INDEX IF NOT EXISTS idx_items_sub ON items(subscription_id)",
            "CREATE INDEX IF NOT EXISTS idx_subs_active ON subscriptions(active, expires_at)",
        ]
        for stmt in statements:
            cur.execute(stmt)
    else:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                email       TEXT    NOT NULL,
                threshold   REAL    NOT NULL DEFAULT 0.10,
                currency    INTEGER NOT NULL DEFAULT 29,
                country     TEXT    NOT NULL DEFAULT 'HK',
                created_at  TEXT    NOT NULL,
                expires_at  TEXT    NOT NULL,
                active      INTEGER NOT NULL DEFAULT 1,
                unsub_token TEXT    NOT NULL UNIQUE,
                language    TEXT    NOT NULL DEFAULT 'zh-TW'
            );
            CREATE TABLE IF NOT EXISTS items (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                subscription_id INTEGER NOT NULL,
                record_index    INTEGER,
                credit          INTEGER NOT NULL,
                transaction_id  TEXT,
                appid           INTEGER NOT NULL,
                item_name       TEXT    NOT NULL,
                price           REAL    NOT NULL,
                listed_date     TEXT,
                action_date     TEXT,
                quantity        INTEGER NOT NULL DEFAULT 1,
                FOREIGN KEY (subscription_id) REFERENCES subscriptions(id) ON DELETE CASCADE
            );
            CREATE TABLE IF NOT EXISTS price_cache (
                item_hash   TEXT    NOT NULL,
                appid       INTEGER NOT NULL,
                lowest      REAL,
                median      REAL,
                volume      TEXT,
                fetched_at  TEXT    NOT NULL,
                PRIMARY KEY (item_hash, appid)
            );
            CREATE INDEX IF NOT EXISTS idx_items_sub ON items(subscription_id);
            CREATE INDEX IF NOT EXISTS idx_subs_active ON subscriptions(active, expires_at);
        """)

    conn.commit()
    conn.close()


# --------------- Subscription helpers ---------------

def create_subscription(email, threshold, currency, country, items_data, language="zh-TW"):
    """
    Create a new subscription and insert parsed items.
    Returns (sub_id, token).
    """
    import secrets

    conn = get_db()
    now = datetime.now(timezone.utc).isoformat()
    expires = (datetime.now(timezone.utc) + timedelta(days=Config.SUBSCRIPTION_DAYS)).isoformat()
    token = secrets.token_urlsafe(32)

    if _use_pg():
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO subscriptions
                (email, threshold, currency, country, created_at, expires_at, unsub_token, language)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (email, threshold, currency, country, now, expires, token, language),
        )
        sub_id = cur.fetchone()["id"]

        for item in items_data:
            cur.execute(
                """
                INSERT INTO items
                    (subscription_id, record_index, credit, transaction_id,
                     appid, item_name, price, listed_date, action_date, quantity)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    sub_id,
                    item.get("record_index"),
                    item["credit"],
                    item.get("transaction_id"),
                    item["appid"],
                    item["item_name"],
                    item["price"],
                    item.get("listed_date"),
                    item.get("action_date"),
                    item.get("quantity", 1),
                ),
            )
    else:
        cursor = conn.execute(
            """INSERT INTO subscriptions
               (email, threshold, currency, country, created_at, expires_at, unsub_token, language)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (email, threshold, currency, country, now, expires, token, language),
        )
        sub_id = cursor.lastrowid

        for item in items_data:
            conn.execute(
                """INSERT INTO items
                   (subscription_id, record_index, credit, transaction_id,
                    appid, item_name, price, listed_date, action_date, quantity)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    sub_id,
                    item.get("record_index"),
                    item["credit"],
                    item.get("transaction_id"),
                    item["appid"],
                    item["item_name"],
                    item["price"],
                    item.get("listed_date"),
                    item.get("action_date"),
                    item.get("quantity", 1),
                ),
            )

    conn.commit()
    conn.close()
    return sub_id, token


def get_active_subscriptions():
    """Return all active, non-expired subscriptions."""
    conn = get_db()
    now = datetime.now(timezone.utc).isoformat()
    cur = _exec(conn, "SELECT * FROM subscriptions WHERE active = 1 AND expires_at > ?", (now,))
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_subscription_items(sub_id):
    """Return all items for a subscription (buy-only, credit=0)."""
    conn = get_db()
    cur = _exec(conn, "SELECT * FROM items WHERE subscription_id = ? AND credit = 0", (sub_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def deactivate_subscription(token):
    """Deactivate a subscription by its unsubscribe token. Returns True if found."""
    conn = get_db()
    cur = _exec(
        conn,
        "UPDATE subscriptions SET active = 0 WHERE unsub_token = ? AND active = 1",
        (token,),
    )
    conn.commit()
    affected = cur.rowcount
    conn.close()
    return affected > 0


def get_subscription_by_token(token):
    """Look up a subscription by unsubscribe token."""
    conn = get_db()
    cur = _exec(conn, "SELECT * FROM subscriptions WHERE unsub_token = ?", (token,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


# --------------- Price cache helpers ---------------

def get_cached_price(item_hash, appid):
    """Get cached price if fresh (< 12 hours old)."""
    conn = get_db()
    cur = _exec(
        conn,
        "SELECT * FROM price_cache WHERE item_hash = ? AND appid = ?",
        (item_hash, appid),
    )
    row = cur.fetchone()
    conn.close()

    if row:
        fetched = datetime.fromisoformat(row["fetched_at"])
        if datetime.now(timezone.utc) - fetched < timedelta(hours=12):
            return dict(row)
    return None


def upsert_price_cache(item_hash, appid, lowest, median, volume):
    """Insert or update a price cache entry."""
    conn = get_db()
    now = datetime.now(timezone.utc).isoformat()
    if _use_pg():
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO price_cache (item_hash, appid, lowest, median, volume, fetched_at)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (item_hash, appid)
            DO UPDATE SET lowest=%s, median=%s, volume=%s, fetched_at=%s
            """,
            (item_hash, appid, lowest, median, volume, now, lowest, median, volume, now),
        )
    else:
        conn.execute(
            """INSERT INTO price_cache (item_hash, appid, lowest, median, volume, fetched_at)
               VALUES (?, ?, ?, ?, ?, ?)
               ON CONFLICT(item_hash, appid)
               DO UPDATE SET lowest=?, median=?, volume=?, fetched_at=?""",
            (item_hash, appid, lowest, median, volume, now, lowest, median, volume, now),
        )
    conn.commit()
    conn.close()


def subscription_day_number(sub):
    """Return which day of the subscription cycle we are on (1-based)."""
    created = datetime.fromisoformat(sub["created_at"])
    now = datetime.now(timezone.utc)
    return max(1, (now - created).days + 1)
