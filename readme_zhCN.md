<div align="center">

<img src="media/logo/steam.svg" alt="Steam" width="64">

# Steam Trader

**上传一次，每天收信，闲置库存帮你盯着**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](#技术栈)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask)](#技术栈)
[![Railway](https://img.shields.io/badge/Deployed%20on-Railway-7B2FBE?style=flat-square&logo=railway&logoColor=white)](https://steamtrader.up.railway.app)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](#)

上传交易记录 · 填写 Email · 每日自动推送行情报告

**[立即使用](https://steamtrader.up.railway.app)**

</div>

> 🌐 **Languages**: [English](readme.md) | [繁體中文](readme_zhHK.md) | 简体中文

---

## 这是什么？

Steam 社区市场本质上是一个庞大的虚拟物品二手交易场。玩家在游戏中自然积累的饰品、箱子、印花，有些自用，有些闲置——它们静静躺在库存里，却可能正处于一个不错的价位。

**Steam Trader 不是量化交易系统，也无意成为一个。** 它更像是你的个人物品管家：帮你记住每件东西花了多少钱买的，现在市场上值多少，扣完手续费还能不能赚一杯奶茶的钱。仅此而已。

> *闲鱼卖家需要一个提醒涨价的工具，而不是一套华尔街交易终端。*

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

整个产品只有**一个页面**和**一封邮件**：

<div align="center">
<img src="media/web_page.png" width="420" alt="Steam Trader 订阅页面">
</div>

用户上传 CSV + 填写 Email → 系统每天定时拉取市场报价，生成静态 HTML 邮件推送。**无需登录，无需注册账号，无需盯着网页看。**

### 核心功能

| 功能 | 描述 |
|------|------|
| **一页上传** | 唯一的前端页面：上传 CSV、填写 Email、设定阈值，提交即走 |
| **每日邮件推送** | 系统自动拉取行情，生成静态 HTML 报告发送至信箱 |
| **出手推荐** | 扣除 Steam 12% 手续费后，筛选收益率达标的物品（阈值可自定义） |
| **30 天周期** | 订阅自动在 30 天后到期，需重新上传 CSV 以刷新持仓数据 |
| **一键退订** | 回复任意邮件即可取消推送 |

### 邮件报告内容

每封推送邮件为静态 HTML，包含：

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Steam Trader · 每日行情报告
  2026-04-15 · 第 12/30 天
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  📊 持仓概览
  ───────────────────────────
  持有物品: 23 件
  估算总市值: ¥ 3,450.00
  值得出手: 5 件

  🔥 推荐出手（收益率 ≥ 10%）
  ┌──────────────────┬────────┬────────┬───────┐
  │ 物品             │ 购入价  │ 当前市价│ 收益率 │
  ├──────────────────┼────────┼────────┼───────┤
  │ AK-47 | Redline  │ ¥40.00 │ ¥52.00 │+14.3% │
  │ AWP | Asiimov    │ ¥150.00│ ¥188.00│+10.2% │
  └──────────────────┴────────┴────────┴───────┘

  📦 全部持仓明细
  (完整物品清单及当前市价)

  ──────────────────────────────────────
  回复本邮件即可取消订阅
  剩余推送天数: 18 天
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 支持的游戏

系统按 CSV 中的 AppID 自动识别，**支持所有拥有 Steam 社区市场的游戏**，包括但不限于：

| AppID | 游戏 |
|------:|------|
| `730` | <img src="media/logo/cs2.svg" alt="CS2" height="16" style="vertical-align:middle"> Counter-Strike 2 |
| `570` | Dota 2 |
| `...` | And any other game with a Community Market |

---

## 技术栈

```
┌──────────────────────────────────────────────────────────┐
│              Frontend（单页）                              │
│   HTML / CSS · Alpine.js                                 │
│   功能: CSV 上传 + Email 输入 + 阈值设定                  │
├──────────────────────────────────────────────────────────┤
│              Backend (Flask 3.x + Gunicorn)              │
│   /upload    接收 CSV + Email                            │
│   /unsubscribe  处理退订                                 │
│   /healthz   健康检查                                    │
├──────────────────────────────┬───────────────────────────┤
│  Data Layer                  │  Scheduler                │
│  pandas · requests · BS4     │  APScheduler              │
│  (行情采集 + 收益率计算)      │  (每日定时触发邮件推送)    │
├──────────────────────────────┼───────────────────────────┤
│  Email                       │  Storage                  │
│  Resend HTTP API             │  PostgreSQL (Railway)     │
│  Jinja2 HTML 模板渲染         │  SQLite (本地开发)         │
├──────────────────────────────┴───────────────────────────┤
│  Deployment                                              │
│  Railway · GitHub CI/CD 自动部署                         │
└──────────────────────────────────────────────────────────┘
```

<details>
<summary><b>依赖明细</b></summary>

| 模块 | 技术 | 职责 |
|------|------|------|
| 后端框架 | Flask 3.x | 路由、文件上传、模板渲染 |
| WSGI 服务器 | Gunicorn | 生产环境部署 |
| 前端 | HTML / CSS / Alpine.js | 单页上传表单 |
| 任务调度 | APScheduler | 每日定时触发推送 |
| 邮件发送 | Resend HTTP API | 生产环境发信（绕过 SMTP 端口限制） |
| 邮件模板 | Jinja2 | 静态 HTML 报告生成 |
| 数据处理 | pandas | CSV 解析、收益率计算 |
| 行情采集 | requests / BeautifulSoup4 | Steam API 调用 |
| 存储（生产） | PostgreSQL | 订阅状态、持仓数据 |
| 存储（本地） | SQLite | 本地开发备用 |
| 部署平台 | Railway | 云端部署、PostgreSQL 插件 |

</details>

---

## 部署

### 线上部署（Railway）

本项目已部署于 [Railway](https://railway.app)，可直接访问：**https://steamtrader.up.railway.app**

如需自行部署，请 Fork 本仓库后，按以下步骤配置 Railway 环境变量：

| 环境变量 | 说明 | 示例值 |
|----------|------|--------|
| `DATABASE_URL` | Railway PostgreSQL 插件自动注入 | *（自动）* |
| `RESEND_API_KEY` | [Resend](https://resend.com) API 密钥 | `re_xxxxxxxx` |
| `MAIL_FROM` | 发件人地址 | `onboarding@resend.dev` |
| `BASE_URL` | 部署后的公开 URL | `https://your-app.up.railway.app` |
| `SECRET_KEY` | Flask Session 密钥 | 任意随机字符串 |
| `DAILY_PUSH_HOUR` | 每日推送时间（UTC） | `10` |

> **邮件服务**：Railway 封锁所有 SMTP 端口，本项目使用 [Resend](https://resend.com) HTTP API（端口 443）发信。免费方案每月 3000 封，未验证域名只能向 Resend 账号绑定的 Email 发信。

### 本地开发

```bash
git clone https://github.com/NokkTsang/SteamTradingAssistant.git
cd SteamTradingAssistant
pip install -r requirements.txt
cp .env.example .env   # 填入 SMTP 或 Resend 配置
python app.py
```

本地开发使用 SQLite，无需 PostgreSQL。邮件可配置 Gmail SMTP（端口 587）作为替代。

## 操作流程

```
 用户操作（一次性）                    系统自动（持续 30 天）
─────────────────                   ─────────────────────
                                    
  Chrome 扩展                        每日定时任务
  导出 CSV                           ┌─────────────────┐
      │                              │ 拉取最新行情     │
      ▼                              │ 计算收益率       │
  打开网页                            │ 渲染 HTML 邮件   │
  上传 CSV + Email ──▶ 系统存储 ──▶  │ 推送至 Email     │
      │                              └────────┬────────┘
      ▼                                       │
  关掉网页,                           第 30 天 ──▶ 自动停止
  完事了                              回复邮件 ──▶ 立即停止
```

### Step 1 — 导出交易历史

1. 在 Chrome 安装 [Steam Market History Cataloger](https://chromewebstore.google.com/detail/steam-market-history-cata/dhpcikljplaooekklhbjohojbjbinega)
2. 进入 Steam 社区市场 → 我的市场历史
3. 扩展自动加载全部记录
4. 点击导出为 CSV

> [!NOTE]
> CSV 表头语言跟随用户的 Steam 账户语言设置自动生成（简体中文账户导出简体表头，英文账户导出英文表头），但**栏位顺序和语义一致**。系统按栏位序号解析，不依赖表头名称。

### Step 2 — 上传并订阅

打开网页，上传 CSV 文件，填写接收邮箱，设定收益率阈值（默认 10%），提交。**然后就可以关掉页面了。**

**栏位定义（以简体中文环境为例）：**

| # | 栏位 | 语义 |
|:-:|------|------|
| 1 | 指数 | 记录序号 |
| 2 | 信用 | `1` = 卖出，`0` = 买入 |
| 3 | 交易ID | Steam 交易唯一标识 |
| 4 | 应用程序ID | 游戏 AppID |
| 5 | 名称 | 物品名称 |
| 6 | 价钱 | 交易金额 |
| 7 | 上市 | 挂牌日期 |
| 8 | 采取行动 | 成交日期 |
| 9 | 金额 | 数量 |

<details>
<summary><b>CSV 示例</b></summary>

```csv
"指数","信用","交易ID","应用程序ID","名称","价钱","上市","采取行动","金额"
119,0,765178889458411703-765178889458411704,730,"印花 | donk（全息，冠军）| 2024年上海锦标赛","¥ 23.40",2025-15-12,2025-15-12,1
```

</details>

### Step 3 — 每天收信

每日固定时间收到一封 HTML 格式的行情报告邮件，内含：

- **持仓概览** — 物品数量、估算总市值
- **出手推荐** — 收益率达标的物品清单（扣除手续费后）
- **全部持仓明细** — 每件物品的购入价 vs 当前市价

### 订阅生命周期

| 事件 | 行为 |
|------|------|
| 上传 CSV + Email | 建立订阅，开始每日推送 |
| 第 30 天 | 自动停止推送 |
| 回复任意推送邮件 | 立即取消订阅 |
| 重新上传 CSV | 刷新持仓数据，重置 30 天周期 |

---

## Steam Market API

Steam 社区市场提供无需鉴权的公开接口，本项目直接调用获取实时报价。

| 接口 | 用途 |
|--------|------|
| `market/priceoverview/` | 获取物品当前最低挂牌价、近期成交中位数、24h 成交量 |
| `market/pricehistory/` | 获取近30 天历史成交价格走势 |

**货币自动识别：** 系统读取 CSV 价格列的货币符号（如 `¥` → CNY/CN、`HK$` → HKD/HK、`$` → USD/US），自动以相同货币向 Steam 市场拉取报价，确保购入价与当前市价在**同一货币**下比较。

**收益率公式：**`(当前市价 × 0.85 − 购入价) ÷ 购入价`（扣除 Steam 15% 手续费）

| 字段 | 来源 | 说明 |
|------|------|------|
| 游戏名 | CSV `AppID` 映射 | 自动识别 |
| 物品名 | Steam API | `market_hash_name` |
| 购入价 | CSV 导入 | 历史交易金额 |
| 最低挂牌价 | Steam API | `lowest_price`（与 CSV 货币一致） |
| 收益率 | 系统计算 | `(市价 × 0.88 − 购入价) ÷ 购入价` |

---

<div align="center">
<sub>Built for fun, not for Wall Street.</sub>
</div>
