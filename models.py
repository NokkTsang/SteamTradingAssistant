import sqlite3
import os
from datetime import datetime, timedelta, timezone
from config import Config


def get_db(db_path=None):
    """Get a database connection with row factory enabled."""
    path = db_path or Config.DATABASE_PATH
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db(db_path=None):
    """Initialize database tables."""
    conn = get_db(db_path)
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
            FOREIGN KEY (subscription_id) REFERENCES subscriptions(id)
                ON DELETE CASCADE
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

        CREATE INDEX IF NOT EXISTS idx_items_sub
            ON items(subscription_id);
        CREATE INDEX IF NOT EXISTS idx_subs_active
            ON subscriptions(active, expires_at);
    """)
    conn.commit()
    conn.close()


# --------------- Subscription helpers ---------------

def create_subscription(email, threshold, currency, country, items_data, language="zh-TW"):
    """
    Create a new subscription and insert parsed items.

    items_data: list of dicts with keys matching the items table columns.
    Returns the subscription id and unsubscribe token.
    """
    import secrets

    conn = get_db()
    now = datetime.now(timezone.utc).isoformat()
    expires = (datetime.now(timezone.utc) + timedelta(days=Config.SUBSCRIPTION_DAYS)).isoformat()
    token = secrets.token_urlsafe(32)

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
    rows = conn.execute(
        "SELECT * FROM subscriptions WHERE active = 1 AND expires_at > ?",
        (now,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_subscription_items(sub_id):
    """Return all items for a subscription (buy-only, credit=0)."""
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM items WHERE subscription_id = ? AND credit = 0",
        (sub_id,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def deactivate_subscription(token):
    """Deactivate a subscription by its unsubscribe token. Returns True if found."""
    conn = get_db()
    cursor = conn.execute(
        "UPDATE subscriptions SET active = 0 WHERE unsub_token = ? AND active = 1",
        (token,),
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected > 0


def get_subscription_by_token(token):
    """Look up a subscription by unsubscribe token."""
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM subscriptions WHERE unsub_token = ?", (token,)
    ).fetchone()
    conn.close()
    return dict(row) if row else None


# --------------- Price cache helpers ---------------

def get_cached_price(item_hash, appid):
    """Get cached price if fresh (< 12 hours old)."""
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM price_cache WHERE item_hash = ? AND appid = ?",
        (item_hash, appid),
    ).fetchone()
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
