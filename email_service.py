import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
from config import Config
from i18n import t, DEFAULT_LANG

logger = logging.getLogger(__name__)

_jinja_env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=True,
)


class _I18nProxy:
    """Allow template access like i.key instead of t('key', lang)."""
    def __init__(self, lang, **extra):
        self._lang = lang
        self._extra = extra
    def __getattr__(self, key):
        return t(key, self._lang, **self._extra.get(key, {}))


def _lang_html(lang):
    return {"en": "en", "zh-HK": "zh-Hant", "zh-CN": "zh-Hans"}.get(lang, "zh-Hant")


def send_report(to_email, report_data, subscription, day_number):
    """
    Render the email report template and send it via SMTP.
    """
    lang = subscription.get("language", DEFAULT_LANG)
    threshold_pct = f"{subscription['threshold'] * 100:.0f}"
    remaining = max(0, Config.SUBSCRIPTION_DAYS - day_number)

    # Build i18n proxy with formatted strings for keys that need parameters
    i = _I18nProxy(lang)

    template = _jinja_env.get_template("email_report.html")
    html_body = template.render(
        report=report_data,
        sub=subscription,
        day=day_number,
        total_days=Config.SUBSCRIPTION_DAYS,
        remaining=remaining,
        threshold_pct=threshold_pct,
        lang_html=_lang_html(lang),
        steam_logo_url=f"{Config.BASE_URL}/media/logo/steam.svg",
        i=type("I18n", (), {
            "email_day_label": t("email_day_label", lang, day=day_number, total=Config.SUBSCRIPTION_DAYS),
            "email_daily_report": t("email_daily_report", lang, pct=threshold_pct),
            "email_items_held": t("email_items_held", lang),
            "email_worth_selling": t("email_worth_selling", lang),
            "email_est_value": t("email_est_value", lang),
            "email_recommend_sell": t("email_recommend_sell", lang, pct=threshold_pct),
            "email_col_item": t("email_col_item", lang),
            "email_col_bought": t("email_col_bought", lang),
            "email_col_current": t("email_col_current", lang),
            "email_col_after_fee": t("email_col_after_fee", lang),
            "email_col_profit": t("email_col_profit", lang),
            "email_no_opportunity": t("email_no_opportunity", lang),
            "email_all_holdings": t("email_all_holdings", lang),
            "email_col_market": t("email_col_market", lang),
            "email_remaining": t("email_remaining", lang),
            "email_remaining_days": t("email_remaining_days", lang, n=remaining),
            "email_unsubscribe": t("email_unsubscribe", lang),
        })(),
    )

    subject = t("email_subject_report", lang, day=day_number, total=Config.SUBSCRIPTION_DAYS)
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = Config.MAIL_FROM
    msg["To"] = to_email

    plain = t("email_plain_report", lang,
              day=day_number,
              total=Config.SUBSCRIPTION_DAYS,
              items=report_data["summary"]["total_items"],
              opps=report_data["summary"]["opportunities_count"],
              value=report_data["summary"]["estimated_value"])
    msg.attach(MIMEText(plain, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    _send_smtp(to_email, msg)


def send_welcome(to_email, subscription):
    """Send a confirmation email after subscription is created."""
    lang = subscription.get("language", DEFAULT_LANG)

    template = _jinja_env.get_template("email_welcome.html")
    html_body = template.render(
        sub=subscription,
        total_days=Config.SUBSCRIPTION_DAYS,
        lang_html=_lang_html(lang),
        steam_logo_url=f"{Config.BASE_URL}/media/logo/steam.svg",
        i=type("I18n", (), {
            "email_welcome_success": t("email_welcome_success", lang),
            "email_welcome_detail": t("email_welcome_detail", lang),
            "email_welcome_email_label": t("email_welcome_email_label", lang),
            "email_welcome_threshold_label": t("email_welcome_threshold_label", lang),
            "email_welcome_cycle_label": t("email_welcome_cycle_label", lang),
            "email_welcome_days": t("email_welcome_days", lang, n=Config.SUBSCRIPTION_DAYS),
            "email_welcome_body": t("email_welcome_body", lang),
            "email_unsubscribe": t("email_unsubscribe", lang),
        })(),
    )

    msg = MIMEMultipart("alternative")
    msg["Subject"] = t("email_subject_welcome", lang)
    msg["From"] = Config.MAIL_FROM
    msg["To"] = to_email

    plain = t("email_plain_welcome", lang, days=Config.SUBSCRIPTION_DAYS)
    msg.attach(MIMEText(plain, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    _send_smtp(to_email, msg)


def _send_smtp(to_email, msg):
    """Low-level SMTP send."""
    if not Config.SMTP_USERNAME or not Config.SMTP_PASSWORD:
        logger.warning("SMTP credentials not configured — email not sent to %s", to_email)
        return

    try:
        with smtplib.SMTP(Config.SMTP_HOST, Config.SMTP_PORT, timeout=30) as server:
            if Config.SMTP_USE_TLS:
                server.starttls()
            server.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
            server.sendmail(Config.MAIL_FROM, [to_email], msg.as_string())
        logger.info("Email sent to %s", to_email)
    except Exception as exc:
        logger.error("Failed to send email to %s: %s", to_email, exc)
        raise
