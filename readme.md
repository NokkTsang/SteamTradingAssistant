<div align="center">

<img src="media/logo/steam.svg" alt="Steam" width="64">

# Steam Trader

**Upload once, get daily emails, we watch your idle inventory**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](#tech-stack)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask)](#tech-stack)
[![Railway](https://img.shields.io/badge/Deployed%20on-Railway-7B2FBE?style=flat-square&logo=railway&logoColor=white)](https://steamtrader.up.railway.app)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](#)

Upload trade history · Enter your email · Receive daily market reports automatically

**[Try It Now](https://steamtrader.up.railway.app)**

</div>

> 🌐 **Languages**: English | [繁體中文](readme_zhHK.md) | [简体中文](readme_zhCN.md)

---

## What Is This?

The Steam Community Market is essentially a massive virtual second-hand marketplace. Players naturally accumulate skins, cases, and stickers through gaming — some are in use, others sit idle in the inventory, potentially at a great selling price.

**Steam Trader is not a quantitative trading system, nor does it intend to be.** Think of it as your personal item butler: it remembers what you paid for each item, tells you what it's worth now, and whether you'd make enough profit after fees for a cup of coffee. That's it.

> *A flea market seller needs a tool that alerts when prices go up, not a Wall Street trading terminal.*

<div align="center">
<table><tr>
<td><img src="media/CS2/AK-47_Aphrodite.webp" width="90" alt="AK-47 Aphrodite"></td>
<td><img src="media/CS2/AK-47_Bloodsport.webp" width="90" alt="AK-47 Bloodsport"></td>
<td><img src="media/CS2/AK-47_Fuel_Injector.webp" width="90" alt="AK-47 Fuel Injector"></td>
<td><img src="media/CS2/AK-47_Vulcan.webp" width="90" alt="AK-47 Vulcan"></td>
<td><img src="media/CS2/AWP_Dragon_Lore.webp" width="90" alt="AWP Dragon Lore"></td>
<td><img src="media/CS2/AWP_Lightning_Strike.webp" width="90" alt="AWP Lightning Strike"></td>
<td><img src="media/CS2/AWP_Printstream.webp" width="90" alt="AWP Printstream"></td>
<td><img src="media/CS2/Bayonet_Autotronic.webp" width="90" alt="Bayonet Autotronic"></td>
<td><img src="media/CS2/Butterfly_Knife_Autotronic.webp" width="90" alt="Butterfly Knife Autotronic"></td>
<td><img src="media/CS2/Butterfly_Knife_Lore.webp" width="90" alt="Butterfly Knife Lore"></td>
</tr><tr>
<td><img src="media/CS2/CS20_Case.webp" width="90" alt="CS20 Case"></td>
<td><img src="media/CS2/Desert_Eagle_Heat_Treated.webp" width="90" alt="Desert Eagle Heat Treated"></td>
<td><img src="media/CS2/Karambit_Fade.webp" width="90" alt="Karambit Fade"></td>
<td><img src="media/CS2/Karambit_Gamma_Doppler.webp" width="90" alt="Karambit Gamma Doppler"></td>
<td><img src="media/CS2/M4A1-S_Fade.webp" width="90" alt="M4A1-S Fade"></td>
<td><img src="media/CS2/M4A1-S_Imminent_Danger.webp" width="90" alt="M4A1-S Imminent Danger"></td>
<td><img src="media/CS2/M4A4_Temukau.webp" width="90" alt="M4A4 Temukau"></td>
<td><img src="media/CS2/M4A4_X-Ray.webp" width="90" alt="M4A4 X-Ray"></td>
<td><img src="media/CS2/Operation_Breakout_Weapon_Case.webp" width="90" alt="Operation Breakout Case"></td>
<td><img src="media/CS2/Sealed_Dead_Hand_Terminal.webp" width="90" alt="Sealed Graffiti"></td>
</tr><tr>
<td><img src="media/CS2/Skeleton_Knife_Blue_Steel.webp" width="90" alt="Skeleton Knife Blue Steel"></td>
<td><img src="media/CS2/Skeleton_Knife_Fade.webp" width="90" alt="Skeleton Knife Fade"></td>
<td><img src="media/CS2/Specialist_Gloves_Fade.webp" width="90" alt="Specialist Gloves Fade"></td>
<td><img src="media/CS2/Sport_Gloves_Amphibious.webp" width="90" alt="Sport Gloves Amphibious"></td>
<td><img src="media/CS2/Sport_Gloves_Ultra_Violent.webp" width="90" alt="Sport Gloves Ultra Violent"></td>
<td><img src="media/CS2/Sticker_Reason_Gaming_(Holo)_Katowice_2014.webp" width="90" alt="Sticker Reason Gaming Holo"></td>
<td><img src="media/CS2/Sticker_Titan_(Holo)_Katowice_2014.webp" width="90" alt="Sticker Titan Holo"></td>
<td><img src="media/CS2/Sticker_Vox_Eminor_(Holo)_Katowice_2014.webp" width="90" alt="Sticker Vox Eminor Holo"></td>
<td><img src="media/CS2/USP-S_Printstream.webp" width="90" alt="USP-S Printstream"></td>
<td><img src="media/CS2/Zeus_x27_Dragon_Snore.webp" width="90" alt="Zeus x27 Dragon Snore"></td>
</tr></table>
</div>

### How It Works

The entire product is **one page** and **one email**:

<div align="center">
<img src="media/web_page.png" width="420" alt="Steam Trader subscription page">
</div>

User uploads CSV + enters email → System fetches market prices daily, generates static HTML email reports. **No login, no account registration, no need to keep a tab open.**

### Core Features

| Feature | Description |
|---------|-------------|
| **Single-page upload** | The only frontend: upload CSV, enter email, set threshold, submit and go |
| **Daily email push** | System auto-fetches market data, generates static HTML report and emails it |
| **Sell recommendations** | Filters items with profit above threshold (after Steam's 12% fee) |
| **30-day cycle** | Subscription auto-expires after 30 days; re-upload CSV to refresh |
| **One-click unsubscribe** | Reply to any email to cancel |

### Email Report Preview

Each push is a static HTML email containing:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Steam Trader · Daily Market Report
  2026-04-15 · Day 12/30
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  📊 Portfolio Overview
  ───────────────────────────
  Items held: 23
  Estimated value: ¥ 3,450.00
  Worth selling: 5

  🔥 Sell Recommendations (profit ≥ 10%)
  ┌──────────────────┬────────┬────────┬───────┐
  │ Item             │ Bought │ Current│ Profit│
  ├──────────────────┼────────┼────────┼───────┤
  │ AK-47 | Redline  │ ¥40.00 │ ¥52.00 │+14.3% │
  │ AWP | Asiimov    │ ¥150.00│ ¥188.00│+10.2% │
  └──────────────────┴────────┴────────┴───────┘

  📦 Full Holdings
  (Complete item list with current prices)

  ──────────────────────────────────────
  Reply to this email to unsubscribe
  Remaining push days: 18
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Supported Games

The system identifies games by AppID in the CSV — **supports all games with a Steam Community Market**, including but not limited to:

| AppID | Game |
|------:|------|
| `730` | <img src="media/logo/cs2.svg" alt="CS2" height="16" style="vertical-align:middle"> Counter-Strike 2 |
| `570` | Dota 2 |
| `...` | And any other game with a Community Market |

---

## Tech Stack

```
┌──────────────────────────────────────────────────────────┐
│              Frontend (Single Page)                       │
│   HTML / CSS · Alpine.js                                 │
│   Features: CSV upload + Email input + Threshold config  │
├──────────────────────────────────────────────────────────┤
│              Backend (Flask 3.x + Gunicorn)              │
│   /upload    Receive CSV + Email                         │
│   /unsubscribe  Handle unsubscription                    │
│   /healthz   Health check                               │
├──────────────────────────────┬───────────────────────────┤
│  Data Layer                  │  Scheduler                │
│  pandas · requests · BS4     │  APScheduler              │
│  (Market data + profit calc) │  (Daily email push cron)  │
├──────────────────────────────┼───────────────────────────┤
│  Email                       │  Storage                  │
│  Resend HTTP API             │  PostgreSQL (Railway)     │
│  Jinja2 HTML template render │  SQLite (local dev)       │
├──────────────────────────────┴───────────────────────────┤
│  Deployment                                              │
│  Railway · GitHub CI/CD auto-deploy                      │
└──────────────────────────────────────────────────────────┘
```

<details>
<summary><b>Dependency Details</b></summary>

| Module | Tech | Role |
|--------|------|------|
| Backend framework | Flask 3.x | Routing, file upload, template rendering |
| WSGI server | Gunicorn | Production deployment |
| Frontend | HTML / CSS / Alpine.js | Single-page upload form |
| Scheduler | APScheduler | Daily cron to trigger push |
| Email sending | Resend HTTP API | Production delivery (bypasses SMTP port blocks) |
| Email templates | Jinja2 | Static HTML report generation |
| Data processing | pandas | CSV parsing, profit calculation |
| Market data | requests / BeautifulSoup4 | Steam API calls |
| Storage (prod) | PostgreSQL | Subscription state, holdings |
| Storage (local) | SQLite | Local development fallback |
| Deployment | Railway | Cloud hosting, PostgreSQL plugin |

</details>

---

## Deployment

### Cloud Deployment (Railway)

This project is deployed on [Railway](https://railway.app) and accessible at: **https://steamtrader.up.railway.app**

To self-host, fork this repository and configure the following Railway environment variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | Auto-injected by Railway PostgreSQL plugin | *(automatic)* |
| `RESEND_API_KEY` | [Resend](https://resend.com) API key | `re_xxxxxxxx` |
| `MAIL_FROM` | Sender email address | `onboarding@resend.dev` |
| `BASE_URL` | Your deployed public URL | `https://your-app.up.railway.app` |
| `SECRET_KEY` | Flask session secret | Any random string |
| `DAILY_PUSH_HOUR` | Daily push time (UTC) | `10` |

> **Email service**: Railway blocks all SMTP ports. This project uses the [Resend](https://resend.com) HTTP API (port 443) to send emails. The free plan allows 3,000 emails/month. Without a verified domain, emails can only be sent to the Resend account's own email address.

### Local Development

```bash
git clone https://github.com/NokkTsang/SteamTradingAssistant.git
cd SteamTradingAssistant
pip install -r requirements.txt
cp .env.example .env   # fill in SMTP or Resend config
python app.py
```

Local dev uses SQLite (`/tmp/steam_trader.db`) — no PostgreSQL required. Gmail SMTP (port 587) can be used as an email alternative.

---

## Workflow

```
 User Action (one-time)                 System (runs for 30 days)
─────────────────────                   ─────────────────────────
                                    
  Chrome Extension                       Daily Cron Job
  Export CSV                             ┌─────────────────┐
      │                                  │ Fetch prices     │
      ▼                                  │ Calculate profit │
  Open webpage                           │ Render HTML email│
  Upload CSV + Email ──▶ System ──▶     │ Push to inbox    │
      │                                  └────────┬────────┘
      ▼                                           │
  Close the page,                        Day 30 ──▶ Auto-stop
  you're done                            Reply email ──▶ Stop now
```

### Step 1 — Export Trade History

1. Install [Steam Market History Cataloger](https://chromewebstore.google.com/detail/steam-market-history-cata/dhpcikljplaooekklhbjohojbjbinega) in Chrome
2. Go to Steam Community Market → My Market History
3. The extension auto-loads all records
4. Click export as CSV

> [!NOTE]
> CSV column headers follow the user's Steam account language setting (e.g., Simplified Chinese accounts export Chinese headers, English accounts export English headers), but **column order and semantics are consistent**. The system parses by column position, not header names.

### Step 2 — Upload and Subscribe

Open the webpage, upload your CSV file, enter your email, set the profit threshold (default 10%), and submit. **Then you can close the page.**

**Field definitions (Simplified Chinese example):**

| # | Field | Meaning |
|:-:|-------|---------|
| 1 | 指数 | Record index |
| 2 | 信用 | `1` = Sell, `0` = Buy |
| 3 | 交易ID | Steam transaction ID |
| 4 | 应用程序ID | Game AppID |
| 5 | 名称 | Item name |
| 6 | 价钱 | Transaction amount |
| 7 | 上市 | Listing date |
| 8 | 采取行动 | Action date |
| 9 | 金额 | Quantity |

<details>
<summary><b>CSV Example</b></summary>

```csv
"指数","信用","交易ID","应用程序ID","名称","价钱","上市","采取行动","金额"
119,0,765178889458411703-765178889458411704,730,"印花 | donk（全息，冠军）| 2024年上海锦标赛","¥ 23.40",2025-14-11,2025-14-11,1
```

</details>

### Step 3 — Receive Daily Emails

You'll receive a static HTML market report email at a fixed time each day, containing:

- **Portfolio Overview** — Item count, estimated total value
- **Sell Recommendations** — Items above profit threshold (after fees)
- **Full Holdings** — Each item's purchase price vs current market price

### Subscription Lifecycle

| Event | Behavior |
|-------|----------|
| Upload CSV + Email | Create subscription, begin daily push |
| Day 30 | Auto-stop push |
| Reply to any push email | Cancel subscription immediately |
| Re-upload CSV | Refresh holdings, reset 30-day cycle |

---

## Steam Market API

The Steam Community Market exposes public, unauthenticated endpoints. This project calls them directly to fetch live pricing.

| Endpoint | Purpose |
|----------|---------|
| `market/priceoverview/` | Current lowest listing price, recent median price, 24h volume |
| `market/pricehistory/` | 30-day historical price trend |

**Automatic currency detection:** The system reads the currency symbol from the CSV price column (e.g. `¥` → CNY/CN, `HK$` → HKD/HK, `$` → USD/US) and queries the Steam Market in the **same currency**, ensuring purchase prices and current market prices are always compared on equal footing.

**Profit formula:** `(current price × 0.85 − purchase price) ÷ purchase price` (after Steam’s 15% fee)

| Field | Source | Description |
|-------|--------|-------------|
| Game name | CSV `AppID` mapping | Auto-detected |
| Item name | Steam API | `market_hash_name` |
| Purchase price | CSV import | Historical transaction amount |
| Lowest listing price | Steam API | `lowest_price` (same currency as CSV) |
| Profit ratio | Calculated | `(price × 0.85 − cost) ÷ cost` |

---

<div align="center">
<sub>Built for fun, not for Wall Street.</sub>
</div>
