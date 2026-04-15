import os
import re
import logging
from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
from config import Config
from models import (
    init_db,
    create_subscription,
    deactivate_subscription,
    get_subscription_by_token,
)
from analyzer import parse_csv
from email_service import send_welcome
from scheduler import start_scheduler
from i18n import t, SUPPORTED_LANGS, DEFAULT_LANG

# --------------- Logging ---------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

# --------------- App factory ---------------
app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.config["MAX_CONTENT_LENGTH"] = Config.MAX_CONTENT_LENGTH

# Ensure upload directory exists
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

# Initialise database on startup
init_db()


# --------------- i18n helper ---------------

class I18nProxy:
    """Allow template access like i.page_subtitle instead of t('page_subtitle', lang)."""
    def __init__(self, lang):
        self._lang = lang
    def __getattr__(self, key):
        return t(key, self._lang)


def _get_lang():
    """Resolve language from query param, form data, or default."""
    lang = request.args.get("lang") or request.form.get("page_lang") or DEFAULT_LANG
    return lang if lang in SUPPORTED_LANGS else DEFAULT_LANG


def _lang_html(lang):
    """Map language code to HTML lang attribute."""
    return {"en": "en", "zh-HK": "zh-Hant", "zh-CN": "zh-Hans"}.get(lang, "zh-Hant")


# --------------- Routes ---------------

@app.route("/", methods=["GET"])
def index():
    """Render the single upload page."""
    lang = _get_lang()
    # Collect CS2 item images for the carousel
    cs2_dir = os.path.join("media", "CS2")
    cs2_images = sorted(f for f in os.listdir(cs2_dir) if f.endswith(".webp")) if os.path.isdir(cs2_dir) else []
    return render_template(
        "index.html",
        default_threshold=int(Config.DEFAULT_THRESHOLD * 100),
        lang=lang,
        lang_html=_lang_html(lang),
        i=I18nProxy(lang),
        cs2_images=cs2_images,
    )


@app.route("/upload", methods=["POST"])
def upload():
    """Handle CSV upload + email subscription."""
    lang = _get_lang()

    # --- Validate language selection for email push ---
    email_lang = request.form.get("language", DEFAULT_LANG)
    if email_lang not in SUPPORTED_LANGS:
        email_lang = DEFAULT_LANG

    # --- Validate email ---
    email = request.form.get("email", "").strip().lower()
    if not email or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        flash(t("flash_invalid_email", lang), "error")
        return redirect(url_for("index", lang=lang))

    # --- Validate threshold ---
    try:
        threshold_pct = int(request.form.get("threshold", "10"))
        if not (0 <= threshold_pct <= 9999):
            raise ValueError
        threshold = threshold_pct / 100.0
    except (ValueError, TypeError):
        flash(t("flash_invalid_threshold", lang), "error")
        return redirect(url_for("index", lang=lang))

    # --- Validate file ---
    file = request.files.get("csv_file")
    if not file or file.filename == "":
        flash(t("flash_no_file", lang), "error")
        return redirect(url_for("index", lang=lang))

    if not file.filename.lower().endswith(".csv"):
        flash(t("flash_csv_only", lang), "error")
        return redirect(url_for("index", lang=lang))

    # --- Parse CSV ---
    try:
        content = file.read()
        items, detected_currency, detected_country = parse_csv(content)
    except ValueError as exc:
        flash(t("flash_csv_error", lang, detail=str(exc)), "error")
        return redirect(url_for("index", lang=lang))
    except Exception:
        logger.exception("Unexpected error parsing CSV")
        flash(t("flash_csv_unexpected", lang), "error")
        return redirect(url_for("index", lang=lang))

    # --- Create subscription ---
    buy_count = sum(1 for i in items if i["credit"] == 0)
    if buy_count == 0:
        flash(t("flash_no_buys", lang), "error")
        return redirect(url_for("index", lang=lang))

    sub_id, token = create_subscription(
        email=email,
        threshold=threshold,
        currency=detected_currency,
        country=detected_country,
        items_data=items,
        language=email_lang,
    )

    logger.info("Subscription %d created for %s — %d items", sub_id, email, len(items))

    # --- Send welcome email ---
    try:
        sub = get_subscription_by_token(token)
        send_welcome(email, sub)
    except Exception:
        logger.exception("Failed to send welcome email")

    flash(
        t("flash_success", lang, count=buy_count, email=email, days=Config.SUBSCRIPTION_DAYS),
        "success",
    )
    return redirect(url_for("index", lang=lang))


@app.route("/unsubscribe/<token>", methods=["GET"])
def unsubscribe(token):
    """Handle unsubscribe via link in email."""
    # Try to get language from the subscription before deactivating
    sub = get_subscription_by_token(token)
    lang = sub["language"] if sub and "language" in sub else DEFAULT_LANG
    if deactivate_subscription(token):
        return render_template("unsubscribed.html", success=True, i=I18nProxy(lang))
    return render_template("unsubscribed.html", success=False, i=I18nProxy(lang))


@app.route("/media/<path:filename>")
def media_file(filename):
    """Serve files from the media directory."""
    return send_from_directory("media", filename)


@app.route("/healthz")
def healthz():
    """Diagnostic endpoint: check DB connection and env vars."""
    import json
    from models import _use_pg, get_db
    info = {
        "db_backend": "postgresql" if _use_pg() else "sqlite",
        "DATABASE_URL_set": bool(Config.DATABASE_URL),
        "SMTP_USERNAME_set": bool(Config.SMTP_USERNAME),
        "SMTP_PASSWORD_set": bool(Config.SMTP_PASSWORD),
        "MAIL_FROM": Config.MAIL_FROM or "(empty)",
        "BASE_URL": Config.BASE_URL,
    }
    try:
        conn = get_db()
        cur = conn.cursor() if _use_pg() else conn.execute("SELECT 1")
        if _use_pg():
            cur.execute("SELECT COUNT(*) as n FROM subscriptions")
            row = cur.fetchone()
            info["subscriptions_count"] = row["n"] if row else "?"
        else:
            info["subscriptions_count"] = conn.execute("SELECT COUNT(*) FROM subscriptions").fetchone()[0]
        conn.close()
        info["db_ok"] = True
    except Exception as e:
        info["db_ok"] = False
        info["db_error"] = str(e)
    return json.dumps(info, indent=2), 200, {"Content-Type": "application/json"}


# --------------- Entry point ---------------

if __name__ == "__main__":
    start_scheduler()
    app.run(host="0.0.0.0", port=5000, debug=False)
