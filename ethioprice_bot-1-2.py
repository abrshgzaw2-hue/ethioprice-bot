import os
import telebot
from telebot import types
from datetime import datetime

BOT_TOKEN   = os.environ.get("BOT_TOKEN", "")
YOUR_CHANNEL = "@ethioprice_et"
ADMIN_ID     = 7059385470  # ያንተ Telegram ID

bot = telebot.TeleBot(BOT_TOKEN)

# ===== ዋጋ ዳታ (በቀላሉ ይቀየራል) =====
prices = {
    "አትክልት 🥦": [
        {"name":"🍅 ቲማቲም",  "en":"Tomato",      "price":45,  "lo":38,  "hi":52,  "unit":"ኪሎ",  "trend":"up"},
        {"name":"🧅 ሽንኩርት", "en":"Onion",       "price":28,  "lo":22,  "hi":35,  "unit":"ኪሎ",  "trend":"down"},
        {"name":"🥬 ጎመን",    "en":"Cabbage",     "price":18,  "lo":14,  "hi":22,  "unit":"ኪሎ",  "trend":"same"},
        {"name":"🥔 ድንች",    "en":"Potato",      "price":22,  "lo":18,  "hi":28,  "unit":"ኪሎ",  "trend":"down"},
        {"name":"🥕 ካሮት",    "en":"Carrot",      "price":30,  "lo":24,  "hi":36,  "unit":"ኪሎ",  "trend":"up"},
        {"name":"🫑 ቃሪያ",    "en":"Bell Pepper", "price":60,  "lo":48,  "hi":70,  "unit":"ኪሎ",  "trend":"up"},
        {"name":"🧄 ነጭ ሽንኩርት","en":"Garlic",   "price":120, "lo":100, "hi":140, "unit":"ኪሎ",  "trend":"up"},
        {"name":"🥒 ኩሽና",    "en":"Cucumber",    "price":20,  "lo":15,  "hi":25,  "unit":"ኪሎ",  "trend":"same"},
    ],
    "ፍራፍሬ 🍊": [
        {"name":"🍌 ሙዝ",     "en":"Banana",  "price":35,  "lo":28, "hi":42,  "unit":"ኪሎ",  "trend":"same"},
        {"name":"🥭 ማንጎ",    "en":"Mango",   "price":40,  "lo":30, "hi":55,  "unit":"ኪሎ",  "trend":"down"},
        {"name":"🍈 ፓፓያ",    "en":"Papaya",  "price":25,  "lo":18, "hi":32,  "unit":"ኪሎ",  "trend":"up"},
        {"name":"🍊 ብርቱካን",  "en":"Orange",  "price":50,  "lo":38, "hi":60,  "unit":"ኪሎ",  "trend":"up"},
        {"name":"🍋 ሎሚ",     "en":"Lemon",   "price":8,   "lo":5,  "hi":12,  "unit":"አንድ", "trend":"down"},
        {"name":"🥑 አቮካዶ",   "en":"Avocado", "price":20,  "lo":15, "hi":25,  "unit":"አንድ", "trend":"same"},
        {"name":"🍎 ፖም",     "en":"Apple",   "price":70,  "lo":55, "hi":85,  "unit":"ኪሎ",  "trend":"down"},
    ],
    "አዝዕርት 🌾": [
        {"name":"🌾 ጤፍ",    "en":"Teff",     "price":95,  "lo":80,  "hi":110, "unit":"ኪሎ", "trend":"up"},
        {"name":"🌿 ስንዴ",   "en":"Wheat",    "price":55,  "lo":45,  "hi":65,  "unit":"ኪሎ", "trend":"down"},
        {"name":"🌽 በቆሎ",   "en":"Maize",    "price":38,  "lo":30,  "hi":45,  "unit":"ኪሎ", "trend":"same"},
        {"name":"🫘 ሽምብራ",  "en":"Chickpea", "price":70,  "lo":60,  "hi":80,  "unit":"ኪሎ", "trend":"up"},
        {"name":"🫘 ምስር",   "en":"Lentil",   "price":65,  "lo":55,  "hi":75,  "unit":"ኪሎ", "trend":"down"},
        {"name":"🍚 ሩዝ",    "en":"Rice",     "price":80,  "lo":70,  "hi":92,  "unit":"ኪሎ", "trend":"up"},
        {"name":"🌾 ማሽላ",   "en":"Sorghum",  "price":42,  "lo":35,  "hi":50,  "unit":"ኪሎ", "trend":"down"},
    ],
    "ሥጋ 🥩": [
        {"name":"🥩 የበሬ ሥጋ",  "en":"Beef",    "price":450, "lo":380, "hi":520, "unit":"ኪሎ",  "trend":"up"},
        {"name":"🐑 የበግ ሥጋ",  "en":"Lamb",    "price":520, "lo":450, "hi":600, "unit":"ኪሎ",  "trend":"up"},
        {"name":"🍗 የዶሮ ሥጋ",  "en":"Chicken", "price":280, "lo":240, "hi":320, "unit":"ኪሎ",  "trend":"down"},
        {"name":"🥚 እንቁላል",   "en":"Egg",     "price":18,  "lo":15,  "hi":22,  "unit":"አንድ", "trend":"up"},
        {"name":"🐟 ዓሣ",      "en":"Fish",    "price":200, "lo":160, "hi":240, "unit":"ኪሎ",  "trend":"same"},
        {"name":"🥛 ወተት",     "en":"Milk",    "price":25,  "lo":20,  "hi":30,  "unit":"ሊትር", "trend":"up"},
    ],
    "ቅመማቅመም 🌶️": [
        {"name":"🌶️ በርበሬ",      "en":"Berbere", "price":180, "lo":140, "hi":220, "unit":"ኪሎ",  "trend":"up"},
        {"name":"🧈 ቅቤ",        "en":"Butter",  "price":650, "lo":580, "hi":720, "unit":"ኪሎ",  "trend":"up"},
        {"name":"🫙 የምግብ ዘይት", "en":"Oil",     "price":120, "lo":100, "hi":140, "unit":"ሊትር", "trend":"down"},
        {"name":"🧂 ጨው",        "en":"Salt",    "price":15,  "lo":12,  "hi":18,  "unit":"ኪሎ",  "trend":"same"},
        {"name":"🍬 ስኳር",       "en":"Sugar",   "price":75,  "lo":65,  "hi":85,  "unit":"ኪሎ",  "trend":"up"},
        {"name":"☕ ቡና",        "en":"Coffee",  "price":220, "lo":180, "hi":260, "unit":"ኪሎ",  "trend":"up"},
    ],
    "ስልኮች 📱": [
        {"name":"📱 Samsung A15",    "en":"Samsung", "price":6500,  "lo":5800,  "hi":7200,  "unit":"ብር", "trend":"up"},
        {"name":"📱 Samsung A55",    "en":"Samsung", "price":18000, "lo":16000, "hi":20000, "unit":"ብር", "trend":"same"},
        {"name":"📱 Samsung S24",    "en":"Samsung", "price":55000, "lo":50000, "hi":60000, "unit":"ብር", "trend":"up"},
        {"name":"📱 Infinix Hot40i", "en":"Infinix", "price":5200,  "lo":4800,  "hi":5800,  "unit":"ብር", "trend":"down"},
        {"name":"📱 Tecno Spark20",  "en":"Tecno",   "price":4800,  "lo":4400,  "hi":5200,  "unit":"ብር", "trend":"up"},
        {"name":"📱 iPhone 14",      "en":"Apple",   "price":65000, "lo":60000, "hi":70000, "unit":"ብር", "trend":"up"},
        {"name":"📱 iPhone 15",      "en":"Apple",   "price":85000, "lo":78000, "hi":92000, "unit":"ብር", "trend":"up"},
        {"name":"📱 Xiaomi Redmi",   "en":"Xiaomi",  "price":7500,  "lo":6800,  "hi":8200,  "unit":"ብር", "trend":"down"},
        {"name":"📱 itel A70",       "en":"itel",    "price":3200,  "lo":2800,  "hi":3600,  "unit":"ብር", "trend":"same"},
    ],
}

trend_icon = {"up":"📈","down":"📉","same":"➡️"}
trend_text = {"up":"ወጣ","down":"ወረደ","same":"ተመሳሳይ"}

def get_date():
    days = ['እሑድ','ሰኞ','ማክሰኞ','ረቡዕ','ሐሙስ','ዓርብ','ቅዳሜ']
    months = ['ጃን','ፌብ','ማር','ኤፕ','ሜይ','ጁን','ጁላ','ኦግ','ሴፕ','ኦክ','ኖቬ','ዲሴ']
    now = datetime.now()
    return f"{days[now.weekday()]} {now.day} {months[now.month-1]} {now.year}"

def format_category(cat):
    items = prices.get(cat, [])
    msg = f"📅 {get_date()}\n{'='*28}\n{cat} — የዕለት ዋጋ\n{'='*28}\n\n"
    for it in items:
        msg += f"{it['name']}\n"
        msg += f"   💰 {it['price']:,} ብር / {it['unit']}\n"
        msg += f"   {trend_icon[it['trend']]} {trend_text[it['trend']]} | ↓{it['lo']:,} — ↑{it['hi']:,}\n\n"
    msg += f"🌐 ethioprice.netlify.app"
    return msg

def format_summary():
    msg = f"🇪🇹 *EthioPrice — የዕለት ዋጋ*\n📅 {get_date()}\n{'─'*26}\n\n"
    for cat, items in prices.items():
        msg += f"*{cat}*\n"
        for it in items[:3]:
            msg += f"  {it['name']}: `{it['price']:,}` ብር/{it['unit']} {trend_icon[it['trend']]}\n"
        msg += "\n"
    msg += "🔗 [ሙሉ ዋጋ](https://ethioprice.netlify.app)"
    return msg

def main_menu():
    m = types.ReplyKeyboardMarkup(resize_keyboard=True)
    m.row("🥦 አትክልት", "🍊 ፍራፍሬ")
    m.row("🌾 አዝዕርት", "🥩 ሥጋ")
    m.row("🌶️ ቅመማቅመም", "📱 ስልኮች")
    m.row("📊 ሁሉም ዋጋ", "ℹ️ ስለ EthioPrice")
    return m

# ===== HANDLERS =====
@bot.message_handler(commands=['start'])
def start(msg):
    name = msg.from_user.first_name or "ጎብኚ"
    bot.send_message(msg.chat.id,
        f"👋 ሰላም {name}!\n\n🇪🇹 *EthioPrice Bot* እንኳን ደህና መጡ!\n\nየዕለት ዋጋ ለማወቅ ከታች ምርጫ ይምረጡ 👇",
        parse_mode="Markdown", reply_markup=main_menu())

@bot.message_handler(commands=['help'])
def help_cmd(msg):
    bot.send_message(msg.chat.id,
        "📖 *EthioPrice እርዳታ*\n\n• ምርት ምረጥ → ዋጋ ያሳያል\n• /start → ዋና ምናሌ\n• /share → ሼር\n\n🌐 ethioprice.netlify.app",
        parse_mode="Markdown")

@bot.message_handler(commands=['share'])
def share_cmd(msg):
    bot.send_message(msg.chat.id,
        f"📢 *EthioPrice ሼር አድርግ!*\n\n👉 t.me/EthioPriceBot\n🌐 ethioprice.netlify.app\n\n🇪🇹 የኢትዮጵያ #1 ዋጋ ማውቂያ!",
        parse_mode="Markdown")

# ===== ADMIN COMMANDS =====
@bot.message_handler(commands=['setprice'])
def set_price(msg):
    if msg.from_user.id != ADMIN_ID:
        bot.send_message(msg.chat.id, "❌ ይህ command ለAdmin ብቻ ነው!")
        return
    try:
        # /setprice ቲማቲም 50
        parts = msg.text.split()
        if len(parts) < 3:
            bot.send_message(msg.chat.id,
                "📝 *አጠቃቀም:*\n`/setprice ምርት-ስም ዋጋ`\n\nምሳሌ:\n`/setprice ቲማቲም 50`\n`/setprice ጤፍ 100`",
                parse_mode="Markdown")
            return
        item_name = parts[1]
        new_price = int(parts[2])
        found = False
        for cat in prices.values():
            for item in cat:
                if item_name in item['name']:
                    old = item['price']
                    item['price'] = new_price
                    if new_price > old:
                        item['trend'] = 'up'
                    elif new_price < old:
                        item['trend'] = 'down'
                    else:
                        item['trend'] = 'same'
                    bot.send_message(msg.chat.id,
                        f"✅ ዋጋ ተቀይሯል!\n\n{item['name']}\n{old:,} ብር → *{new_price:,} ብር*",
                        parse_mode="Markdown")
                    found = True
                    break
        if not found:
            bot.send_message(msg.chat.id, f"❌ '{item_name}' አልተገኘም!\n\nምርቱን በትክክል ጻፍ።")
    except Exception as e:
        bot.send_message(msg.chat.id, f"❌ Error: {e}\n\nምሳሌ: `/setprice ቲማቲም 50`", parse_mode="Markdown")

@bot.message_handler(commands=['prices'])
def show_all_prices(msg):
    if msg.from_user.id != ADMIN_ID:
        return
    text = "📋 *ሁሉም ምርቶች (Admin)*\n\n"
    for cat, items in prices.items():
        text += f"*{cat}*\n"
        for it in items:
            text += f"  • {it['name']}: {it['price']:,} ብር\n"
        text += "\n"
    bot.send_message(msg.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['post'])
def post_to_channel(msg):
    if msg.from_user.id != ADMIN_ID:
        bot.send_message(msg.chat.id, "❌ Admin ብቻ!")
        return
    try:
        bot.send_message(YOUR_CHANNEL, format_summary(), parse_mode="Markdown")
        bot.send_message(msg.chat.id, "✅ Channel ላይ ተለጠፈ!")
    except Exception as e:
        bot.send_message(msg.chat.id, f"❌ Error: {e}")

@bot.message_handler(commands=['admin'])
def admin_help(msg):
    if msg.from_user.id != ADMIN_ID:
        return
    bot.send_message(msg.chat.id,
        "🔧 *Admin Commands*\n\n"
        "`/setprice ቲማቲም 50` — ዋጋ ቀይር\n"
        "`/prices` — ሁሉም ዋጋ ዝርዝር\n"
        "`/post` — Channel ላይ ለጥፍ\n"
        "`/admin` — ይህ ምናሌ\n\n"
        "✅ አንተ ብቻ ነህ የምትጠቀምበት!",
        parse_mode="Markdown")

@bot.message_handler(func=lambda m: True)
def handle(msg):
    t = msg.text.strip() if msg.text else ""
    if "አትክልት" in t:
        bot.send_message(msg.chat.id, format_category("አትክልት 🥦"), reply_markup=main_menu())
    elif "ፍራፍሬ" in t:
        bot.send_message(msg.chat.id, format_category("ፍራፍሬ 🍊"), reply_markup=main_menu())
    elif "አዝዕርት" in t:
        bot.send_message(msg.chat.id, format_category("አዝዕርት 🌾"), reply_markup=main_menu())
    elif "ሥጋ" in t or "ስጋ" in t:
        bot.send_message(msg.chat.id, format_category("ሥጋ 🥩"), reply_markup=main_menu())
    elif "ቅመማቅመም" in t:
        bot.send_message(msg.chat.id, format_category("ቅመማቅመም 🌶️"), reply_markup=main_menu())
    elif "ስልኮች" in t or "ሥልኮች" in t:
        bot.send_message(msg.chat.id, format_category("ስልኮች 📱"), reply_markup=main_menu())
    elif "ሁሉም" in t or "📊" in t:
        bot.send_message(msg.chat.id, format_summary(), parse_mode="Markdown", reply_markup=main_menu())
    elif "ስለ" in t or "ℹ️" in t:
        bot.send_message(msg.chat.id,
            "🌿 *ስለ EthioPrice*\n\nየኢትዮጵያ ሁሉም ከተሞች የዕለት ዋጋ\n\n🌐 ethioprice.netlify.app",
            parse_mode="Markdown", reply_markup=main_menu())
    else:
        bot.send_message(msg.chat.id, "👇 ከታች ምርጫ ተጫን", reply_markup=main_menu())

print("🚀 EthioPrice Bot እየሠራ ነው...")
bot.infinity_polling()
