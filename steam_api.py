import re
import time
import logging
import requests
from config import Config
from models import get_cached_price, upsert_price_cache

logger = logging.getLogger(__name__)

# Map of common AppIDs to game names
APPID_GAMES = {
    730: "Counter-Strike 2",
    570: "Dota 2",
    440: "Team Fortress 2",
    578080: "PUBG: BATTLEGROUNDS",
    252490: "Rust",
    753: "Steam",
}


class SteamMarketAPI:
    """Thin wrapper around Steam Community Market public endpoints."""

    BASE_URL = "https://steamcommunity.com/market"

    def __init__(self, currency=None, country=None, interval=None):
        self.currency = currency or Config.STEAM_CURRENCY
        self.country = country or Config.STEAM_COUNTRY
        self.interval = interval or Config.STEAM_REQUEST_INTERVAL
        self._last_request = 0.0

    # ---- rate limiting ----

    def _wait(self):
        elapsed = time.time() - self._last_request
        if elapsed < self.interval:
            time.sleep(self.interval - elapsed)
        self._last_request = time.time()

    # ---- public methods ----

    def get_price(self, item_hash_name, appid=730):
        """
        Fetch price overview for a single item.
        Returns dict with keys: lowest, median, volume  (all numeric or None).
        Uses local cache to avoid redundant requests.
        """
        cached = get_cached_price(item_hash_name, appid)
        if cached:
            return {
                "lowest": cached["lowest"],
                "median": cached["median"],
                "volume": cached["volume"],
            }

        self._wait()
        try:
            resp = requests.get(
                f"{self.BASE_URL}/priceoverview/",
                params={
                    "country": self.country,
                    "currency": self.currency,
                    "appid": appid,
                    "market_hash_name": item_hash_name,
                },
                timeout=10,
            )
            resp.raise_for_status()
            data = resp.json()
        except Exception as exc:
            logger.warning("Steam API error for %s: %s", item_hash_name, exc)
            return None

        if not data.get("success"):
            return None

        lowest = self._parse_price(data.get("lowest_price", ""))
        median = self._parse_price(data.get("median_price", ""))
        volume = data.get("volume", "0")

        upsert_price_cache(item_hash_name, appid, lowest, median, volume)

        return {"lowest": lowest, "median": median, "volume": volume}

    def get_price_history(self, item_hash_name, appid=730, days=30):
        """Fetch price history (requires Steam login cookie — optional feature)."""
        self._wait()
        try:
            resp = requests.get(
                f"{self.BASE_URL}/pricehistory/",
                params={"appid": appid, "market_hash_name": item_hash_name},
                timeout=10,
            )
            resp.raise_for_status()
            data = resp.json()
        except Exception as exc:
            logger.warning("Price history error for %s: %s", item_hash_name, exc)
            return []

        if "prices" not in data:
            return []

        return [
            {"date": e[0], "price": float(e[1]), "volume": int(e[2])}
            for e in data["prices"][-days:]
        ]

    # ---- helpers ----

    @staticmethod
    def _parse_price(price_str):
        """Extract numeric value from price string like 'HK$ 52.00' or '¥ 23.40'."""
        if not price_str:
            return None
        match = re.search(r"[\d,]+\.?\d*", price_str.replace(" ", ""))
        if match:
            return float(match.group().replace(",", ""))
        return None

    @staticmethod
    def game_name(appid):
        """Resolve AppID to a human-readable game name."""
        return APPID_GAMES.get(appid, f"App {appid}")
