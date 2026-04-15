"""
Internationalization (i18n) support for Steam Trader.
Supports: English (en), Traditional Chinese (zh-HK), Simplified Chinese (zh-CN).
"""

SUPPORTED_LANGS = ["en", "zh-HK", "zh-CN"]
DEFAULT_LANG = "zh-HK"

STRINGS = {
    # ── Upload page (index.html) ──
    "page_title": {
        "en": "Steam Trader",
        "zh-HK": "Steam Trader",
        "zh-CN": "Steam Trader",
    },
    "page_subtitle": {
        "en": "Upload trade history, get daily market reports via email<br>We watch your idle inventory for you",
        "zh-HK": "上傳交易記錄，每天收到行情報告郵件<br>閒置庫存幫你盯著",
        "zh-CN": "上传交易记录，每天收到行情报告邮件<br>闲置库存帮你盯着",
    },
    "label_csv": {
        "en": "Trade History CSV",
        "zh-HK": "交易記錄 CSV",
        "zh-CN": "交易记录 CSV",
    },
    "file_placeholder": {
        "en": "Click or drop CSV file here",
        "zh-HK": "點擊或拖放 CSV 文件",
        "zh-CN": "点击或拖放 CSV 文件",
    },
    "label_email": {
        "en": "Email Address",
        "zh-HK": "接收郵箱",
        "zh-CN": "接收邮箱",
    },
    "label_threshold": {
        "en": "Profit Threshold",
        "zh-HK": "收益率閾值",
        "zh-CN": "收益率阈值",
    },
    "threshold_suffix": {
        "en": "% or above to recommend selling",
        "zh-HK": "% 以上推薦出手",
        "zh-CN": "% 以上推荐出手",
    },
    "label_language": {
        "en": "Email Language",
        "zh-HK": "郵件語言",
        "zh-CN": "邮件语言",
    },
    "btn_subscribe": {
        "en": "Start Subscription",
        "zh-HK": "開始訂閱",
        "zh-CN": "开始订阅",
    },
    "info_daily_push": {
        "en": "Daily market report delivered to your inbox",
        "zh-HK": "每日自動推送行情報告到你的信箱",
        "zh-CN": "每日自动推送行情报告到你的信箱",
    },
    "info_30_days": {
        "en": "Auto-stops after 30 days, re-upload to refresh",
        "zh-HK": "30 天後自動停止，需重新上傳刷新",
        "zh-CN": "30 天后自动停止，需重新上传刷新",
    },
    "info_unsubscribe": {
        "en": "Reply to any email to unsubscribe",
        "zh-HK": "隨時回覆郵件取消訂閱",
        "zh-CN": "随时回复邮件取消订阅",
    },
    "info_csv_source": {
        "en": "CSV exported via",
        "zh-HK": "CSV 由",
        "zh-CN": "CSV 由",
    },
    "info_csv_source_suffix": {
        "en": "",
        "zh-HK": "導出",
        "zh-CN": "导出",
    },

    # ── Flash messages (app.py) ──
    "flash_invalid_email": {
        "en": "Please enter a valid email address.",
        "zh-HK": "請輸入有效的 Email 地址。",
        "zh-CN": "请输入有效的 Email 地址。",
    },
    "flash_invalid_threshold": {
        "en": "Profit threshold must be an integer between 0 and 9999.",
        "zh-TW": "收益率閾值必須是 0–9999 之間的整數。",
        "zh-CN": "收益率阈值必须是 0–9999 之间的整数。",
    },
    "flash_no_file": {
        "en": "Please select a CSV file.",
        "zh-HK": "請選擇 CSV 文件。",
        "zh-CN": "请选择 CSV 文件。",
    },
    "flash_csv_only": {
        "en": "Only .csv files are supported.",
        "zh-HK": "僅支持 .csv 格式的文件。",
        "zh-CN": "仅支持 .csv 格式的文件。",
    },
    "flash_csv_error": {
        "en": "CSV parse failed: {detail}",
        "zh-HK": "CSV 解析失敗：{detail}",
        "zh-CN": "CSV 解析失败：{detail}",
    },
    "flash_csv_unexpected": {
        "en": "An error occurred while parsing the CSV. Please check the file format.",
        "zh-HK": "CSV 解析時發生錯誤，請確認文件格式。",
        "zh-CN": "CSV 解析时发生错误，请确认文件格式。",
    },
    "flash_no_buys": {
        "en": "No purchase records (credit=0) found in CSV. Please check the file.",
        "zh-HK": "CSV 中沒有找到購入記錄（信用=0），請確認文件內容。",
        "zh-CN": "CSV 中没有找到购入记录（信用=0），请确认文件内容。",
    },
    "flash_success": {
        "en": "Subscribed! Imported {count} purchase records. Daily reports will be sent to {email} for {days} days.",
        "zh-HK": "訂閱成功！已導入 {count} 筆購入記錄。每日行情報告將發送至 {email}，持續 {days} 天。",
        "zh-CN": "订阅成功！已导入 {count} 笔购入记录。每日行情报告将发送至 {email}，持续 {days} 天。",
    },

    # ── Email report ──
    "email_subject_report": {
        "en": "Steam Trader · Daily Report · Day {day}/{total}",
        "zh-HK": "Steam Trader · 每日行情報告 · 第 {day}/{total} 天",
        "zh-CN": "Steam Trader · 每日行情报告 · 第 {day}/{total} 天",
    },
    "email_daily_report": {
        "en": "Daily Market Report · Profit threshold ≥ {pct}%",
        "zh-HK": "每日行情報告 · 收益率閾值 ≥ {pct}%",
        "zh-CN": "每日行情报告 · 收益率阈值 ≥ {pct}%",
    },
    "email_day_label": {
        "en": "Day {day}/{total}",
        "zh-HK": "第 {day}/{total} 天",
        "zh-CN": "第 {day}/{total} 天",
    },
    "email_items_held": {
        "en": "Items Held",
        "zh-HK": "持有物品",
        "zh-CN": "持有物品",
    },
    "email_worth_selling": {
        "en": "Worth Selling",
        "zh-HK": "值得出手",
        "zh-CN": "值得出手",
    },
    "email_est_value": {
        "en": "Est. Value",
        "zh-HK": "估算市值",
        "zh-CN": "估算市值",
    },
    "email_recommend_sell": {
        "en": "🔥 Recommended to Sell (profit ≥ {pct}%)",
        "zh-HK": "🔥 推薦出手（收益率 ≥ {pct}%）",
        "zh-CN": "🔥 推荐出手（收益率 ≥ {pct}%）",
    },
    "email_col_item": {
        "en": "Item",
        "zh-HK": "物品",
        "zh-CN": "物品",
    },
    "email_col_bought": {
        "en": "Bought",
        "zh-HK": "購入價",
        "zh-CN": "购入价",
    },
    "email_col_current": {
        "en": "Current",
        "zh-HK": "當前市價",
        "zh-CN": "当前市价",
    },
    "email_col_after_fee": {
        "en": "After Fee",
        "zh-HK": "到手",
        "zh-CN": "到手",
    },
    "email_col_profit": {
        "en": "Profit",
        "zh-HK": "收益率",
        "zh-CN": "收益率",
    },
    "email_no_opportunity": {
        "en": "No selling opportunities today. Hold on 📦",
        "zh-HK": "今日暫無達到閾值的出手機會，繼續持有觀望 📦",
        "zh-CN": "今日暂无达到阈值的出手机会，继续持有观望 📦",
    },
    "email_all_holdings": {
        "en": "📦 All Holdings",
        "zh-HK": "📦 全部持倉明細",
        "zh-CN": "📦 全部持仓明细",
    },
    "email_col_market": {
        "en": "Market",
        "zh-HK": "市價",
        "zh-CN": "市价",
    },
    "email_remaining": {
        "en": "Remaining push days:",
        "zh-HK": "剩餘推送天數:",
        "zh-CN": "剩余推送天数:",
    },
    "email_remaining_days": {
        "en": "{n} days",
        "zh-HK": "{n} 天",
        "zh-CN": "{n} 天",
    },
    "email_unsubscribe": {
        "en": "Unsubscribe",
        "zh-HK": "取消訂閱",
        "zh-CN": "取消订阅",
    },
    "email_plain_report": {
        "en": "Steam Trader Daily Report (Day {day}/{total})\n"
              "Items held: {items}\nWorth selling: {opps}\n"
              "Estimated value: {value}\n\n"
              "View the full report in an HTML-capable email client.",
        "zh-HK": "Steam Trader 每日行情報告 (第 {day}/{total} 天)\n"
                  "持有物品: {items} 件\n值得出手: {opps} 件\n"
                  "估算總市值: {value}\n\n"
                  "查看完整報告請使用支持 HTML 郵件的客戶端。",
        "zh-CN": "Steam Trader 每日行情报告 (第 {day}/{total} 天)\n"
                  "持有物品: {items} 件\n值得出手: {opps} 件\n"
                  "估算总市值: {value}\n\n"
                  "查看完整报告请使用支持 HTML 邮件的客户端。",
    },

    # ── Welcome email ──
    "email_subject_welcome": {
        "en": "Steam Trader · Subscription Confirmed",
        "zh-HK": "Steam Trader · 訂閱確認",
        "zh-CN": "Steam Trader · 订阅确认",
    },
    "email_welcome_success": {
        "en": "✓ Subscription Confirmed",
        "zh-HK": "✓ 訂閱成功",
        "zh-CN": "✓ 订阅成功",
    },
    "email_welcome_detail": {
        "en": "Your subscription details:",
        "zh-HK": "你的訂閱詳情：",
        "zh-CN": "你的订阅详情：",
    },
    "email_welcome_email_label": {
        "en": "Email",
        "zh-HK": "接收郵箱",
        "zh-CN": "接收邮箱",
    },
    "email_welcome_threshold_label": {
        "en": "Profit threshold",
        "zh-HK": "收益率閾值",
        "zh-CN": "收益率阈值",
    },
    "email_welcome_cycle_label": {
        "en": "Push cycle",
        "zh-HK": "推送週期",
        "zh-CN": "推送周期",
    },
    "email_welcome_days": {
        "en": "{n} days",
        "zh-HK": "{n} 天",
        "zh-CN": "{n} 天",
    },
    "email_welcome_body": {
        "en": "Starting tomorrow, you'll receive a daily market report.<br>"
              "To unsubscribe, click the link below or reply to any push email.",
        "zh-HK": "從明天開始，你將每天收到一封行情報告郵件。<br>"
                  "如需取消訂閱，點擊下方連結或回覆任意推送郵件。",
        "zh-CN": "从明天开始，你将每天收到一封行情报告邮件。<br>"
                  "如需取消订阅，点击下方链接或回复任意推送邮件。",
    },
    "email_plain_welcome": {
        "en": "You have subscribed to Steam Trader daily reports.\n"
              "Push will last {days} days.\nReply to unsubscribe.",
        "zh-HK": "你已成功訂閱 Steam Trader 每日行情推送。\n"
                  "推送將持續 {days} 天。\n回覆此郵件即可取消訂閱。",
        "zh-CN": "你已成功订阅 Steam Trader 每日行情推送。\n"
                  "推送将持续 {days} 天。\n回复此邮件即可取消订阅。",
    },

    # ── Unsubscribe page ──
    "unsub_title_success": {
        "en": "Unsubscribed ✓",
        "zh-HK": "已取消訂閱 ✓",
        "zh-CN": "已取消订阅 ✓",
    },
    "unsub_body_success": {
        "en": "You will no longer receive daily reports.<br>To re-subscribe, upload your CSV again.",
        "zh-HK": "你將不再收到每日行情報告。<br>如需重新訂閱，請再次上傳 CSV。",
        "zh-CN": "你将不再收到每日行情报告。<br>如需重新订阅，请再次上传 CSV。",
    },
    "unsub_title_fail": {
        "en": "Invalid Link",
        "zh-HK": "連結無效",
        "zh-CN": "链接无效",
    },
    "unsub_body_fail": {
        "en": "This subscription may have already been cancelled or expired.",
        "zh-HK": "該訂閱可能已取消或已過期。",
        "zh-CN": "该订阅可能已取消或已过期。",
    },
    "unsub_back_home": {
        "en": "← Back to Home",
        "zh-HK": "← 返回首頁",
        "zh-CN": "← 返回首页",
    },
}


def t(key, lang=None, **kwargs):
    """
    Get a translated string.
    Falls back to zh-HK if key or lang not found.
    Supports keyword formatting: t("flash_success", lang="en", count=5, email="x@y.com", days=30)
    """
    if lang not in SUPPORTED_LANGS:
        lang = DEFAULT_LANG
    entry = STRINGS.get(key, {})
    text = entry[lang] if lang in entry else entry.get(DEFAULT_LANG, key)
    if kwargs:
        text = text.format(**kwargs)
    return text
