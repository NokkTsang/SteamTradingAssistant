import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration loaded from environment variables."""

    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(32).hex())
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2 MB upload limit

    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "")  # PostgreSQL on Railway
    DATABASE_PATH = os.getenv("DATABASE_PATH", "/tmp/steam_trader.db")  # SQLite fallback

    # Steam API
    STEAM_CURRENCY = int(os.getenv("STEAM_CURRENCY", "29"))  # 29 = HKD
    STEAM_COUNTRY = os.getenv("STEAM_COUNTRY", "HK")
    STEAM_REQUEST_INTERVAL = float(os.getenv("STEAM_REQUEST_INTERVAL", "1.5"))

    # Email (SMTP)
    SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USE_TLS = os.getenv("SMTP_USE_TLS", "true").lower() == "true"
    SMTP_USERNAME = os.getenv("SMTP_USERNAME", "")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
    MAIL_FROM = os.getenv("MAIL_FROM", SMTP_USERNAME)

    # Subscription
    SUBSCRIPTION_DAYS = int(os.getenv("SUBSCRIPTION_DAYS", "30"))
    DEFAULT_THRESHOLD = float(os.getenv("DEFAULT_THRESHOLD", "0.10"))

    # Scheduler
    DAILY_PUSH_HOUR = int(os.getenv("DAILY_PUSH_HOUR", "10"))
    DAILY_PUSH_MINUTE = int(os.getenv("DAILY_PUSH_MINUTE", "0"))

    # Upload
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")

    # Base URL (for email asset links)
    BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")
