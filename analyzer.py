import io
import re
import logging
import pandas as pd
from steam_api import SteamMarketAPI

logger = logging.getLogger(__name__)

STEAM_FEE_RATE = 0.15  # Steam takes 15% (publisher fee + Steam fee combined)

# Map price string prefix → (Steam currency code, country code)
_CURRENCY_MAP = [
    ("HK$",  29, "HK"),
    ("US$",   1, "US"),
    ("€",     3, "DE"),
    ("£",     2, "GB"),
    ("¥",    23, "CN"),   # also matches ￥
    ("￥",   23, "CN"),
    ("₩",   16, "KR"),
    ("R$",   7, "BR"),
    ("$",     1, "US"),   # fallback plain $
]


def _detect_currency(price_str: str):
    """Return (steam_currency_code, country) from a raw price string, or (29, 'HK') as default."""
    s = price_str.strip()
    for prefix, code, country in _CURRENCY_MAP:
        if s.startswith(prefix) or prefix in s:
            return code, country
    return 29, "HK"  # default HKD


def parse_csv(file_content: bytes):
    """
    Parse a Steam Market History Cataloger CSV (any language header).
    Columns are identified by position, not by header name.

    Returns a list of dicts ready for database insertion.
    """
    # Try common encodings
    for encoding in ("utf-8-sig", "utf-8", "gbk", "latin-1"):
        try:
            text = file_content.decode(encoding)
            break
        except (UnicodeDecodeError, ValueError):
            continue
    else:
        raise ValueError("Unable to decode CSV file. Please ensure it is UTF-8 encoded.")

    df = pd.read_csv(io.StringIO(text))

    if df.shape[1] < 9:
        raise ValueError(f"CSV must have at least 9 columns, found {df.shape[1]}.")

    # Rename columns by position regardless of language
    col_map = {
        df.columns[0]: "record_index",
        df.columns[1]: "credit",
        df.columns[2]: "transaction_id",
        df.columns[3]: "appid",
        df.columns[4]: "item_name",
        df.columns[5]: "price_str",
        df.columns[6]: "listed_date",
        df.columns[7]: "action_date",
        df.columns[8]: "quantity",
    }
    df = df.rename(columns=col_map)

    items = []
    detected_currency, detected_country = 29, "HK"  # will be overwritten on first valid price
    currency_detected = False
    for _, row in df.iterrows():
        price_raw = str(row["price_str"])
        price = _parse_price_str(price_raw)
        if price is None:
            continue

        if not currency_detected:
            detected_currency, detected_country = _detect_currency(price_raw)
            currency_detected = True

        items.append(
            {
                "record_index": int(row["record_index"]) if pd.notna(row["record_index"]) else None,
                "credit": int(row["credit"]),
                "transaction_id": str(row["transaction_id"]) if pd.notna(row["transaction_id"]) else None,
                "appid": int(row["appid"]),
                "item_name": str(row["item_name"]).strip(),
                "price": price,
                "listed_date": str(row["listed_date"]) if pd.notna(row["listed_date"]) else None,
                "action_date": str(row["action_date"]) if pd.notna(row["action_date"]) else None,
                "quantity": int(row["quantity"]) if pd.notna(row["quantity"]) else 1,
            }
        )

    if not items:
        raise ValueError("No valid items found in CSV.")

    logger.info("CSV currency detected: code=%d country=%s", detected_currency, detected_country)
    return items, detected_currency, detected_country


def analyze_portfolio(items, threshold=0.10, currency=29, country="HK"):
    """
    Given a list of *purchased* items (credit=0), fetch current prices
    and compute profit ratios.

    Returns a dict with:
      - summary: {total_items, total_cost, estimated_value, opportunities_count}
      - opportunities: list of items with profit_ratio >= threshold
      - holdings: all items with current price info
    """
    api = SteamMarketAPI(currency=currency, country=country)

    holdings = []
    opportunities = []
    total_cost = 0.0
    estimated_value = 0.0

    for item in items:
        price_data = api.get_price(item["item_name"], item["appid"])

        current_price = price_data["lowest"] if price_data and price_data["lowest"] else None
        median_price = price_data["median"] if price_data and price_data["median"] else None
        volume = price_data["volume"] if price_data else "N/A"

        bought_price = item["price"]
        total_cost += bought_price

        profit_ratio = None
        after_fee = None
        if current_price and bought_price > 0:
            after_fee = current_price * (1 - STEAM_FEE_RATE)
            profit_ratio = (after_fee - bought_price) / bought_price
            estimated_value += current_price

        entry = {
            "item_name": item["item_name"],
            "appid": item["appid"],
            "game": SteamMarketAPI.game_name(item["appid"]),
            "bought_price": bought_price,
            "current_price": current_price,
            "median_price": median_price,
            "after_fee": round(after_fee, 2) if after_fee else None,
            "profit_ratio": profit_ratio,
            "profit_pct": f"{profit_ratio * 100:+.1f}%" if profit_ratio is not None else "N/A",
            "volume": volume,
        }
        holdings.append(entry)

        if profit_ratio is not None and profit_ratio >= threshold:
            opportunities.append(entry)

    # Sort opportunities by profit ratio descending
    opportunities.sort(key=lambda x: x["profit_ratio"] or 0, reverse=True)
    holdings.sort(key=lambda x: x["profit_ratio"] or -999, reverse=True)

    return {
        "summary": {
            "total_items": len(holdings),
            "total_cost": round(total_cost, 2),
            "estimated_value": round(estimated_value, 2),
            "opportunities_count": len(opportunities),
        },
        "opportunities": opportunities,
        "holdings": holdings,
    }


def _parse_price_str(s):
    """Extract a float from a price string like '¥ 23.40' or 'HK$ 52.00'."""
    match = re.search(r"[\d,]+\.?\d*", s.replace(" ", ""))
    if match:
        return float(match.group().replace(",", ""))
    return None
