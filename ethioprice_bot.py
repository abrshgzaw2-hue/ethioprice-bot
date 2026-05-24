"""
EthioPrice Telegram Bot
=======================
ይህን ፋይል ለማሂድ:
1. pip install pytelegrambotapi
2. YOUR_BOT_TOKEN ቀይር
3. YOUR_CHANNEL ቀይር (ለምሳሌ: @ethioprice_et)
4. python ethioprice_bot.py
"""

import telebot
from telebot import types
from datetime import datetime

# ===== ይህን ቀይር =====
YOUR_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"   # BotFather ከሰጠህ token
YOUR_CHANNEL   = "@ethioprice_et"         # ያንተ channel username
# ====================

bot = telebot.TeleBot(YOUR_BOT_TOKEN)

# ===== ዋጋ ዳታ =====
prices = {
    "አትክልት 🥦": [
        ("🍅 ቲማቲም",    45,  38,  52,  "ኪሎ",  "up"),
        ("🧅 ሽንኩርት",   28,  22,  35,  "ኪሎ",  "down"),
        ("🥬 ጎመን",      18,  14,  22,  "ኪሎ",  "same"),
        ("🥔 ድንች",      22,  18,  28,  "ኪሎ",  "down"),
        ("🥕 ካሮት",      30,  24,  36,  "ኪሎ",  "up"),
        ("🫑 ቃሪያ",      60,  48,  70,  "ኪሎ",  "up"),
        ("🧄 ነጭ ሽንኩርት",120, 100, 140, "ኪሎ",  "up"),
        ("🥒 ኩሽና",      20,  15,  25,  "ኪሎ",  "same"),
    ],
    "ፍራፍሬ 🍊": [
        ("🍌 ሙዝ",       35,  28,  42,  "ኪሎ",  "same"),
        ("🥭 ማንጎ",      40,  30,  55,  "ኪሎ",  "down"),
        ("🍈 ፓፓያ",      25,  18,  32,  "ኪሎ",  "up"),
        ("🍊 ብርቱካን",    50,  38,  60,  "ኪሎ",  "up"),
        ("🍋 ሎሚ",        8,   5,  12,  "አንድ", "down"),
        ("🥑 አቮካዶ",     20,  15,  25,  "አንድ", "same"),
        ("🍎 ፖም",        70,  55,  85,  "ኪሎ",  "down"),
    ],
    "አዝዕርት 🌾": [
        ("🌾 ጤፍ",        95,  80, 110,  "ኪሎ",  "up"),
        ("🌿 ስንዴ",       55,  45,  65,  "ኪሎ",  "down"),
        ("🌽 በቆሎ",       38,  30,  45,  "ኪሎ",  "same"),
        ("🫘 ሽምብራ",      70,  60,  80,  "ኪሎ",  "up"),
        ("🫘 ምስር",        65,  55,  75,  "ኪሎ",  "down"),
        ("🍚 ሩዝ",         80,  70,  92,  "ኪሎ",  "up"),
        ("🌾 ማሽላ",       42,  35,  50,  "ኪሎ",  "down"),
    ],
    "ሥጋ 🥩": [
        ("🥩 የበሬ ሥጋ",  450, 380, 520,  "ኪሎ",  "up"),
        ("🐑 የበግ ሥጋ",  520, 450, 600,  "ኪሎ",  "up"),
        ("🍗 የዶሮ ሥጋ",  280, 240, 320,  "ኪሎ",  "down"),
        ("🥚 እንቁላል",    18,  15,  22,  "አንድ", "up"),
        ("🐟 ዓሣ ቲላፒያ", 200, 160, 240, "ኪሎ",  "same"),
        ("🥛 ወተት",       25,  20,  30,  "ሊትር", "up"),
    ],
    "ቅመማቅመም 🌶️": [
        ("🌶️ በርበሬ",    180, 140, 220,  "ኪሎ",  "up"),
        ("🧈 ቅቤ",       650, 580, 720,  "ኪሎ",  "up"),
        ("🫙 የምግብ ዘይት",120, 100, 140, "ሊትር", "down"),
        ("🧂 ጨው",        15,  12,  18,  "ኪሎ",  "same"),
        ("🍬 ስኳር",       75,  65,  85,  "ኪሎ",  "up"),
        ("☕ ቡና",        220, 180, 260,  "ኪሎ",  "up"),
    ],
    "ስልኮች 📱": [
        ("📱 Samsung A15",   6500,  5800,  7200, "ብር", "up"),
        ("📱 Samsung A55",  18000, 16000, 20000, "ብር", "same"),
        ("📱 Samsung S24",  55000, 50000, 60000, "ብር", "up"),
        ("📱 Infinix Hot40i", 5200, 4800, 5800, "ብር", "down"),
        ("📱 Tecno Spark20",  4800, 4400, 5200, "ብር", "up"),
        ("📱 iPhone 14",    65000, 60000, 70000, "ብር", "up"),
        ("📱 iPhone 15",    85000, 78000, 92000, "ብር", "up"),
        ("📱 Xiaomi Redmi",  7500,  6800,  8200, "ብር", "down"),
        ("📱 itel A70",      3200,  2800,  3600, "ብር", "same"),
    ],
}

trend_icon = {"up": "📈", "down": "📉", "same": "➡️"}
trend_text = {"up": "ወጣ", "down": "ወረደ", "same": "ተመሳሳይ"}

def get_date():
    days = ['እሑድ','ሰኞ','ማክሰኞ','ረቡዕ','ሐሙስ','ዓርብ','ቅዳሜ']
    months = ['ጃን','ፌብ','ማር','ኤፕ','ሜይ','ጁን','ጁላ','ኦግ','ሴፕ','ኦክ','ኖቬ','ዲሴ']
    now = datetime.now()
    return f"{days[now.weekday()]} {now.day} {months[now.month-1]} {now.year}"

def format_price_list(category):
    items = prices.get(category, [])
    today = get_date()
    msg = f"📅 {today}\n"
    msg += f"{'='*30}\n"
    msg += f"{category} — የዕለት ዋጋ\n"
    msg += f"{'='*30}\n\n"
    for name, price, lo, hi, unit, trend in items:
        icon = trend_icon[trend]
        ttext = trend_text[trend]
        msg += f"{name}\n"
        msg += f"   💰 {price:,} ብር / {unit}\n"
        msg += f"   {icon} {ttext} | ↓{lo:,} — ↑{hi:,}\n\n"
    msg += f"🌐 ethioprice.netlify.app"
    return msg

def format_all_summary():
    today = get_date()
    msg = f"🇪🇹 *EthioPrice — የዕለት ዋጋ ማጠቃለያ*\n"
    msg += f"📅 {today}\n"
    msg += f"{'─'*28}\n\n"
    for cat, items in prices.items():
        msg += f"*{cat}*\n"
        for name, price, lo, hi, unit, trend in items[:3]:
            icon = trend_icon[trend]
            msg += f"  {name}: `{price:,}` ብር/{unit} {icon}\n"
        msg += "\n"
    msg += f"🔗 [ሙሉ ዋጋ ለማየት](https://ethioprice.netlify.app)"
    return msg

# ===== MAIN MENU =====
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🥦 አትክልት", "🍊 ፍራፍሬ")
    markup.row("🌾 አዝዕርት", "🥩 ሥጋ")
    markup.row("🌶️ ቅመማቅመም", "📱 ስልኮች")
    markup.row("📊 ሁሉም ዋጋ", "ℹ️ ስለ EthioPrice")
    return markup

# ===== HANDLERS =====
@bot.message_handler(commands=['start'])
def start(msg):
    name = msg.from_user.first_name or "ጎብኚ"
    text = (
        f"👋 ሰላም {name}!\n\n"
        f"🇪🇹 *EthioPrice Bot* እንኳን ደህና መጡ!\n\n"
        f"የዕለት ዋጋ ለማወቅ ከታች ያለውን ምርጫ ተጫኑ 👇"
    )
    bot.send_message(msg.chat.id, text, parse_mode="Markdown", reply_markup=main_menu())

@bot.message_handler(commands=['help'])
def help_cmd(msg):
    text = (
        "📖 *EthioPrice Bot እርዳታ*\n\n"
        "• ምርት ምረጥ → ዋጋ ያሳያል\n"
        "• 📊 ሁሉም ዋጋ → ሁሉም ምርቶች\n"
        "• /start → ወደ ዋና ምናሌ\n"
        "• /share → Channel ለጓደኞች ሼር\n\n"
        "🌐 ethioprice.netlify.app"
    )
    bot.send_message(msg.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['share'])
def share_cmd(msg):
    text = (
        "📢 *EthioPrice ለጓደኞችህ ሼር አድርግ!*\n\n"
        f"👉 Bot: t.me/ethioprice_bot\n"
        f"👉 Channel: {YOUR_CHANNEL}\n"
        f"👉 Website: ethioprice.netlify.app\n\n"
        "🇪🇹 የኢትዮጵያ #1 ዋጋ ማውቂያ!"
    )
    bot.send_message(msg.chat.id, text, parse_mode="Markdown")

@bot.message_handler(func=lambda m: True)
def handle_text(msg):
    txt = msg.text.strip()

    if "አትክልት" in txt:
        bot.send_message(msg.chat.id, format_price_list("አትክልት 🥦"), reply_markup=main_menu())
    elif "ፍራፍሬ" in txt:
        bot.send_message(msg.chat.id, format_price_list("ፍራፍሬ 🍊"), reply_markup=main_menu())
    elif "አዝዕርት" in txt:
        bot.send_message(msg.chat.id, format_price_list("አዝዕርት 🌾"), reply_markup=main_menu())
    elif "ሥጋ" in txt or "ስጋ" in txt:
        bot.send_message(msg.chat.id, format_price_list("ሥጋ 🥩"), reply_markup=main_menu())
    elif "ቅመማቅመም" in txt:
        bot.send_message(msg.chat.id, format_price_list("ቅመማቅመም 🌶️"), reply_markup=main_menu())
    elif "ስልኮች" in txt or "ሥልኮች" in txt:
        bot.send_message(msg.chat.id, format_price_list("ስልኮች 📱"), reply_markup=main_menu())
    elif "ሁሉም" in txt or "📊" in txt:
        bot.send_message(msg.chat.id, format_all_summary(), parse_mode="Markdown", reply_markup=main_menu())
    elif "ስለ" in txt or "ℹ️" in txt:
        text = (
            "🌿 *ስለ EthioPrice*\n\n"
            "EthioPrice የኢትዮጵያ ሁሉም ከተሞች የዕለት ዋጋ ያሳያል።\n\n"
            "• አትክልት ና ፍራፍሬ\n"
            "• አዝዕርት ና ሥጋ\n"
            "• ቅመማቅመም\n"
            "• ስልኮች\n\n"
            "🌐 ethioprice.netlify.app\n"
            f"📢 {YOUR_CHANNEL}"
        )
        bot.send_message(msg.chat.id, text, parse_mode="Markdown", reply_markup=main_menu())
    else:
        bot.send_message(msg.chat.id,
            "❓ ምን ማወቅ ትፈልጋለህ?\nከታች ያለውን ምርጫ ተጫን 👇",
            reply_markup=main_menu())

# ===== CHANNEL POSTER (manual) =====
def post_to_channel():
    """ይህን function በየቀኑ channel ላይ ለመለጠፍ ጥቀም"""
    msg = format_all_summary()
    bot.send_message(YOUR_CHANNEL, msg, parse_mode="Markdown")
    print("✅ Channel ላይ ተለጠፈ!")

# ===== RUN =====
print("🚀 EthioPrice Bot እየሠራ ነው...")
print(f"📢 Channel: {YOUR_CHANNEL}")
bot.infinity_polling()
