<div align="center">

<img src="media/logo/steam.svg" alt="Steam" width="64">

# Steam Trader

**上傳一次，每天收信，閒置庫存幫你盯著**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](#技術棧)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask)](#技術棧)
[![Railway](https://img.shields.io/badge/Deployed%20on-Railway-7B2FBE?style=flat-square&logo=railway&logoColor=white)](https://steamtrader.up.railway.app)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](#)

上傳交易記錄 · 填寫 Email · 每日自動推送行情報告

**[立即使用](https://steamtrader.up.railway.app)**

</div>

> 🌐 **Languages**: [English](readme.md) | 繁體中文 | [简体中文](readme_zhCN.md)

---

## 這是什麼？

Steam 社區市場本質上是一個龐大的虛擬物品二手交易場。玩家在遊戲中自然積累的飾品、箱子、印花，有些自用，有些閒置——它們靜靜躺在庫存裡，卻可能正處於一個不錯的價位。

**Steam Trader 不是量化交易系統，也無意成為一個。** 它更像是你的個人物品管家：幫你記住每件東西花了多少錢買的，現在市場上值多少，扣完手續費還能不能賺一杯奶茶的錢，僅此而已。

> *閒魚賣家需要一個提醒漲價的工具，而不是一套華爾街交易終端。*

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

### 工作方式

整個產品只有**一個頁面**和**一封郵件**：

<div align="center">
<img src="media/web_page.png" width="420" alt="Steam Trader 訂閱頁面">
</div>

用戶上傳 CSV + 填寫 Email → 系統每天定時拉取市場報價，生成靜態 HTML 郵件推送。**無需登錄，無需註冊帳號，無需盯著網頁看。**

### 核心功能

| 功能 | 描述 |
|------|------|
| **一頁上傳** | 唯一的前端頁面：上傳 CSV、填寫 Email、設定閾值，提交即走 |
| **每日郵件推送** | 系統自動拉取行情，生成靜態 HTML 報告發送至信箱 |
| **出手推薦** | 扣除 Steam 12% 手續費後，篩選收益率達標的物品（閾值可自定義） |
| **30 天週期** | 訂閱自動在 30 天後到期，需重新上傳 CSV 以刷新持倉數據 |
| **一鍵退訂** | 回覆任意郵件即可取消推送 |

### 郵件報告內容

每封推送郵件為靜態 HTML，包含：

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Steam Trader · 每日行情報告
  2026-04-15 · 第 12/30 天
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  📊 持倉概覽
  ───────────────────────────
  持有物品: 23 件
  估算總市值: ¥ 3,450.00
  值得出手: 5 件

  🔥 推薦出手（收益率 ≥ 10%）
  ┌──────────────────┬────────┬────────┬───────┐
  │ 物品             │ 購入價  │當前市價 │ 收益率 │
  ├──────────────────┼────────┼────────┼───────┤
  │ AK-47 | Redline  │ ¥40.00 │ ¥52.00 │+14.3% │
  │ AWP | Asiimov    │ ¥150.00│ ¥188.00│+10.2% │
  └──────────────────┴────────┴────────┴───────┘

  📦 全部持倉明細
  (完整物品清單及當前市價)

  ──────────────────────────────────────
  回覆本郵件即可取消訂閱
  剩餘推送天數: 18 天
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 支持的遊戲

系統按 CSV 中的 AppID 自動識別，**支持所有擁有 Steam 社區市場的遊戲**，包括但不限於：

| AppID | 遊戲 |
|------:|------|
| `730` | <img src="media/logo/cs2.svg" alt="CS2" height="16" style="vertical-align:middle"> Counter-Strike 2 |
| `570` | Dota 2 |
| `...` | 以及其他具有社區市場的遊戲 |

---

## 技術棧

```
┌──────────────────────────────────────────────────────────┐
│              Frontend (單頁)                              │
│   HTML / CSS · Alpine.js                                 │
│   功能: CSV 上傳 + Email 輸入 + 閾值設定                  │
├──────────────────────────────────────────────────────────┤
│              Backend (Flask 3.x + Gunicorn)              │
│   /upload    接收 CSV + Email                            │
│   /unsubscribe  處理退訂                                 │
│   /healthz   健康檢查                                    │
├──────────────────────────────┬───────────────────────────┤
│  Data Layer                  │  Scheduler                │
│  pandas · requests · BS4     │  APScheduler              │
│  (行情採集 + 收益率計算)      │  (每日定時觸發郵件推送)    │
├──────────────────────────────┼───────────────────────────┤
│  Email                       │  Storage                  │
│  Resend HTTP API             │  PostgreSQL (Railway)     │
│  Jinja2 HTML 模板渲染         │  SQLite (本地開發)         │
├──────────────────────────────┴───────────────────────────┤
│  Deployment                                              │
│  Railway · GitHub CI/CD 自動部署                         │
└──────────────────────────────────────────────────────────┘
```

<details>
<summary><b>依賴明細</b></summary>

| 模塊 | 技術 | 職責 |
|------|------|------|
| 後端框架 | Flask 3.x | 路由、文件上傳、模板渲染 |
| WSGI 服務器 | Gunicorn | 生產環境部署 |
| 前端 | HTML / CSS / Alpine.js | 單頁上傳表單 |
| 任務調度 | APScheduler | 每日定時觸發推送 |
| 郵件發送 | Resend HTTP API | 生產環境發信（繞過 SMTP 端口限制） |
| 郵件模板 | Jinja2 | 靜態 HTML 報告生成 |
| 數據處理 | pandas | CSV 解析、收益率計算 |
| 行情採集 | requests / BeautifulSoup4 | Steam API 調用 |
| 存儲（生產） | PostgreSQL | 訂閱狀態、持倉數據 |
| 存儲（本地） | SQLite | 本地開發備用 |
| 部署平台 | Railway | 雲端部署、PostgreSQL 插件 |

</details>

---

## 部署

### 線上部署（Railway）

本項目已部署於 [Railway](https://railway.app)，可直接訪問：**https://steamtrader.up.railway.app**

如需自行部署，請 Fork 本倉庫後，按以下步驟配置 Railway 環境變量：

| 環境變量 | 說明 | 範例值 |
|----------|------|--------|
| `DATABASE_URL` | Railway PostgreSQL 插件自動注入 | *(自動)* |
| `RESEND_API_KEY` | [Resend](https://resend.com) API 密鑰 | `re_xxxxxxxx` |
| `MAIL_FROM` | 發件人地址 | `onboarding@resend.dev` |
| `BASE_URL` | 部署後的公開 URL | `https://your-app.up.railway.app` |
| `SECRET_KEY` | Flask Session 密鑰 | 任意隨機字符串 |
| `DAILY_PUSH_HOUR` | 每日推送時間（UTC） | `10` |

> **郵件服務**：Railway 封鎖所有 SMTP 端口，本項目使用 [Resend](https://resend.com) HTTP API（端口 443）發信。免費方案每月 3000 封，需驗證域名才能向任意收件人發信；未驗證域名只能發送至 Resend 帳號綁定的 Email。

### 本地開發

```bash
git clone https://github.com/NokkTsang/SteamTradingAssistant.git
cd SteamTradingAssistant
pip install -r requirements.txt
cp .env.example .env   # 填入 SMTP 或 Resend 配置
python app.py
```

本地開發使用 SQLite（`/tmp/steam_trader.db`），無需 PostgreSQL。郵件可配置 Gmail SMTP（端口 587）作為替代。

---

## 操作流程

```
 用戶操作 (一次性)                    系統自動 (持續 30 天)
─────────────────                   ─────────────────────
                                    
  Chrome 擴展                        每日定時任務
  導出 CSV                           ┌─────────────────┐
      │                              │ 拉取最新行情     │
      ▼                              │ 計算收益率       │
  打開網頁                            │ 渲染 HTML 郵件   │
  上傳 CSV + Email ──▶ 系統存儲 ──▶  │ 推送至 Email     │
      │                              └────────┬────────┘
      ▼                                       │
  關掉網頁,                           第 30 天 ──▶ 自動停止
  完事了                              回覆郵件 ──▶ 立即停止
```

### Step 1 — 導出交易歷史

1. 在 Chrome 安裝 [Steam Market History Cataloger](https://chromewebstore.google.com/detail/steam-market-history-cata/dhpcikljplaooekklhbjohojbjbinega)
2. 進入 Steam 社區市場 → 我的市場歷史
3. 擴展自動加載全部記錄
4. 點擊導出為 CSV

> [!NOTE]
> CSV 表頭語言跟隨用戶的 Steam 帳戶語言設置自動生成（簡體中文帳戶導出簡體表頭，英文帳戶導出英文表頭），但**欄位順序和語義一致**。系統按欄位序號解析，不依賴表頭名稱。

### Step 2 — 上傳並訂閱

打開網頁，上傳 CSV 文件，填寫接收郵箱，設定收益率閾值（默認 10%），提交。**然後就可以關掉頁面了。**

**欄位定義（以簡體中文環境為例）：**

| # | 欄位 | 語義 |
|:-:|------|------|
| 1 | 指数 | 記錄序號 |
| 2 | 信用 | `1` = 賣出，`0` = 買入 |
| 3 | 交易ID | Steam 交易唯一標識 |
| 4 | 应用程序ID | 遊戲 AppID |
| 5 | 名称 | 物品名稱 |
| 6 | 价钱 | 交易金額 |
| 7 | 上市 | 掛牌日期 |
| 8 | 采取行动 | 成交日期 |
| 9 | 金额 | 數量 |

<details>
<summary><b>CSV 示例</b></summary>

```csv
"指数","信用","交易ID","应用程序ID","名称","价钱","上市","采取行动","金额"
119,0,765178889458411703-765178889458411704,730,"印花 | donk（全息，冠军）| 2024年上海锦标赛","¥ 23.40",2025-1-12,2025-1-12,1
```

</details>

### Step 3 — 每天收信

每日固定時間收到一封 HTML 格式的行情報告郵件，內含：

- **持倉概覽** — 物品數量、估算總市值
- **出手推薦** — 收益率達標的物品清單（扣除手續費後）
- **全部持倉明細** — 每件物品的購入價 vs 當前市價

### 訂閱生命週期

| 事件 | 行為 |
|------|------|
| 上傳 CSV + Email | 建立訂閱，開始每日推送 |
| 第 30 天 | 自動停止推送 |
| 回覆任意推送郵件 | 立即取消訂閱 |
| 重新上傳 CSV | 刷新持倉數據，重置 30 天週期 |

---

## Steam Market API

Steam 社區市場提供無需鑑權的公開接口，本項目直接調用獲取即時報價。

| 接口 | 用途 |
|--------|------|
| `market/priceoverview/` | 獲取物品目前最低掛牌價、近期成交中位數、24h 成交量 |
| `market/pricehistory/` | 獲取近 30 天歷史成交價格走勢 |

**貨幣自動債測：** 系統讀取 CSV 价格欄的貨幣符號（如 `¥` → CNY/CN、`HK$` → HKD/HK、`$` → USD/US），自動以相同貨幣向 Steam 市場拉取報價，確保購入價與當前市價在**同一貨幣**下比較。

**收益率公式：**`(當前市價 × 0.85 − 購入價) ÷ 購入價`（扣除 Steam 15% 手續費）

| 變數 | 來源 | 說明 |
|------|------|------|
| 適勎名 | CSV `AppID` 映射 | 自動識別 |
| 物品名 | Steam API | `market_hash_name` |
| 購入價 | CSV 匯入 | 歷史交易金額 |
| 最低掛牌價 | Steam API | `lowest_price`（與 CSV 貨幣一致） |
| 收益率 | 系統計算 | `(市價 × 0.85 − 購入價) ÷ 購入價` |

---

<div align="center">
<sub>Built for fun, not for Wall Street.</sub>
</div>
