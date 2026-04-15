<div align="center">

<img src="media/logo/steam.svg" alt="Steam" width="64">
&nbsp;&nbsp;&nbsp;
<img src="media/logo/cs2.svg" alt="CS2" width="64">

# Steam Trader

**上傳一次，每天收信，閒置庫存幫你盯著**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](#技術棧)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask)](#技術棧)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](#)

上傳交易記錄 · 填寫 Email · 每日自動推送行情報告

</div>

> 🌐 **Language / 語言**: [English](readme_en.md) | 繁體中文 | [简体中文](readme_zhCN.md)

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
| `730` | Counter-Strike 2 |
| `570` | Dota 2 |
| `440` | Team Fortress 2 |
| `578080` | PUBG: BATTLEGROUNDS |
| `252490` | Rust |
| `...` | 以及其他具有社區市場的遊戲 |

---

## 技術棧

```
┌──────────────────────────────────────────────────────────┐
│              Frontend (單頁)                              │
│   HTML / CSS · 原生 JS 或 Alpine.js                      │
│   功能: CSV 上傳 + Email 輸入 + 閾值設定                  │
├──────────────────────────────────────────────────────────┤
│              Backend (Flask 3.x)                         │
│   /upload    接收 CSV + Email                            │
│   /unsubscribe  處理退訂                                 │
├──────────────────────────────┬───────────────────────────┤
│  Data Layer                  │  Scheduler                │
│  pandas · requests · BS4     │  APScheduler              │
│  (行情採集 + 收益率計算)      │  (每日定時觸發郵件推送)    │
├──────────────────────────────┴───────────────────────────┤
│  Email                       │  Storage                  │
│  Flask-Mail / SMTP           │  SQLite                   │
│  Jinja2 HTML 模板渲染         │  (訂閱記錄·持倉·報價緩存)  │
└──────────────────────────────────────────────────────────┘
```

<details>
<summary><b>依賴明細</b></summary>

| 模塊 | 技術 | 職責 |
|------|------|------|
| 後端框架 | Flask 3.x | 路由、文件上傳、模板渲染 |
| 前端 | HTML / CSS / Alpine.js | 單頁上傳表單（無需構建工具） |
| 任務調度 | APScheduler | 每日定時遍歷活躍訂閱、觸發推送 |
| 郵件發送 | Flask-Mail / smtplib | SMTP 發信、HTML 郵件渲染 |
| 郵件模板 | Jinja2 | 靜態 HTML 報告生成 |
| 數據處理 | pandas | CSV 解析、收益率計算 |
| 行情採集 | requests / BeautifulSoup4 | Steam API 調用、頁面解析 |
| 存儲 | SQLite | 訂閱狀態、持倉數據、報價緩存 |

</details>

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
119,0,765178889458411703-765178889458411704,730,"印花 | donk（全息，冠军）| 2024年上海锦标赛","¥ 23.40",2025-14-12,2025-14-12,1
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

## 核心模塊

### Steam 市場 API — 行情採集

Steam 社區市場提供無需鑑權的公開接口：

```python
import requests

def get_steam_price(item_hash_name, appid=730):
    """
    獲取 Steam 市場物品價格
    appid=730 → CS2, currency=29 → 港幣
    """
    url = "https://steamcommunity.com/market/priceoverview/"
    params = {
        "country": "HK",
        "currency": "29",
        "appid": appid,
        "market_hash_name": item_hash_name
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("success"):
        return {
            "lowest_price": data.get("lowest_price"),   # 最低掛牌價
            "median_price": data.get("median_price"),   # 近期成交中位數
            "volume": data.get("volume")                # 24h 成交量
        }
    return None
```

### 交易分析引擎

```python
import pandas as pd

class TradingAnalyzer:
    STEAM_FEE_RATE = 0.12  # Steam 手續費 12%

    def __init__(self, history_csv_path):
        self.history = pd.read_csv(history_csv_path)

    def calculate_profit_ratio(self, bought_price, current_price):
        """
        收益率 = (到手金額 - 購入成本) / 購入成本
        到手金額 = 當前市價 × (1 - 手續費率)
        """
        after_fee = current_price * (1 - self.STEAM_FEE_RATE)
        return (after_fee - bought_price) / bought_price

    def find_sell_opportunities(self, items, threshold=0.10):
        """篩選收益率 ≥ threshold 的物品"""
        opportunities = []
        for item in items:
            current_price = get_steam_price(item['hash_name'])
            ratio = self.calculate_profit_ratio(
                item['bought_price'],
                current_price['lowest_price']
            )
            if ratio >= threshold:
                opportunities.append({
                    'item_name': item['name'],
                    'bought_price': item['bought_price'],
                    'current_price': current_price['lowest_price'],
                    'profit_ratio': f"{ratio * 100:.1f}%",
                    'after_fee_income': current_price['lowest_price'] * 0.88,
                    'listing_count': current_price.get('listing_count', 'N/A')
                })
        return opportunities
```

### 趨勢數據

```python
def get_price_history(item_hash_name, days=30):
    """拉取近 N 天歷史成交數據"""
    url = "https://steamcommunity.com/market/pricehistory/"
    params = {"appid": 730, "market_hash_name": item_hash_name}

    response = requests.get(url, params=params)
    data = response.json()

    return [
        {'date': e[0], 'price': float(e[1]), 'volume': int(e[2])}
        for e in data['prices'][-days:]
    ]
```

---

## 數據字段映射

| 字段 | 來源 | 說明 |
|------|------|------|
| 遊戲名 | CSV `AppID` 映射 | 自動識別 |
| 物件名 | Steam API | `market_hash_name` |
| 品質 / 磨損 | 市場頁面解析 | Factory New → Battle-Scarred |
| 購入價 | CSV 導入 | 歷史交易金額 |
| 出售價 | CSV 導入 | 已成交則顯示 |
| 掛牌量 | 市場頁面解析 | 當前在售數量 |
| 最低掛牌價 | Steam API | `lowest_price` |
| 收益率 | 系統計算 | `(市價 × 0.88 − 購入價) ÷ 購入價` |
| 趨勢圖 | 歷史價格 API | 近 30 天價格走勢 |

---

<div align="center">
<sub>Built for fun, not for Wall Street.</sub>
</div>