import logging
from apscheduler.schedulers.background import BackgroundScheduler
from config import Config
from models import (
    get_active_subscriptions,
    get_subscription_items,
    subscription_day_number,
)
from analyzer import analyze_portfolio
from email_service import send_report

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler(daemon=True)


def daily_push_job():
    """
    Iterate over all active subscriptions, analyze each portfolio,
    and send an email report.
    """
    logger.info("Starting daily push job...")
    subscriptions = get_active_subscriptions()
    logger.info("Found %d active subscription(s).", len(subscriptions))

    for sub in subscriptions:
        try:
            items = get_subscription_items(sub["id"])
            if not items:
                logger.info("Subscription %d has no buy items, skipping.", sub["id"])
                continue

            day = subscription_day_number(sub)
            logger.info(
                "Processing subscription %d (%s) — day %d/%d",
                sub["id"], sub["email"], day, Config.SUBSCRIPTION_DAYS,
            )

            report = analyze_portfolio(
                items,
                threshold=sub["threshold"],
                currency=sub["currency"],
                country=sub["country"],
            )

            send_report(sub["email"], report, sub, day)

        except Exception:
            logger.exception("Error processing subscription %d", sub["id"])


def start_scheduler():
    """Register the daily job and start the background scheduler."""
    scheduler.add_job(
        daily_push_job,
        trigger="cron",
        hour=Config.DAILY_PUSH_HOUR,
        minute=Config.DAILY_PUSH_MINUTE,
        id="daily_push",
        replace_existing=True,
    )
    scheduler.start()
    logger.info(
        "Scheduler started — daily push at %02d:%02d UTC",
        Config.DAILY_PUSH_HOUR,
        Config.DAILY_PUSH_MINUTE,
    )
