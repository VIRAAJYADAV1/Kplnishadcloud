import asyncio
import logging
from datetime import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes, ChatMemberHandler
import json
import os
import random

# ═══════════════════════════════════════════
# KPL CLOUD SELLER BOT
# Owner: @kplboy
# Admin: @VIRAAJYADAV_247
# ═══════════════════════════════════════════

BOT_TOKEN = "8520478105:AAHmcF-PYvIvuq_5IqQudpdeqeTJOg1cczE"

# Owner & Admin Details
OWNER_USERNAME = "@kplboy"
OWNER_WHATSAPP = "+91 82188 29942"
ADMIN_USERNAME = "@VIRAAJYADAV_247"

# File to store group IDs
GROUPS_FILE = "groups.json"

def load_groups():
    if os.path.exists(GROUPS_FILE):
        with open(GROUPS_FILE, "r") as f:
            return json.load(f)
    return []

def save_groups(groups):
    with open(GROUPS_FILE, "w") as f:
        json.dump(groups, f)

# ═══════════════════════════════════════════
# PROMOTIONAL MESSAGES (Rotates randomly)
# ═══════════════════════════════════════════

PROMO_MESSAGES = [
    """🌐 *KPL CLOUD SELLER* 🌐
━━━━━━━━━━━━━━━━━━━━

☁️ *Premium Cloud Accounts Available!*

☁️ AWS (Amazon Web Services)
🔵 Microsoft Azure Portal
🟡 Google Cloud Platform (GCP)
🔷 DigitalOcean

━━━━━━━━━━━━━━━━━━━━
💰 *Best Prices in Market*
⚡ *Instant Delivery*
🛡️ *100% Trusted*
🔄 *Replacement Guarantee*
━━━━━━━━━━━━━━━━━━━━

📩 *Owner:* """ + OWNER_USERNAME + """
📱 *WhatsApp:* """ + OWNER_WHATSAPP + """

_DM now to get your cloud account!_""",

    """🔥 *FLASH SALE - CLOUD ACCOUNTS* 🔥
━━━━━━━━━━━━━━━━━━━━

🚀 *Available Platforms:*

1️⃣ ☁️ AWS Portal
2️⃣ 🔵 Azure Portal  
3️⃣ 🟡 Google Cloud
4️⃣ 🔷 DigitalOcean

✅ Fresh & Verified Accounts
✅ With Free Credits
✅ Full Access
✅ Instant Delivery
✅ After-Sale Support

━━━━━━━━━━━━━━━━━━━━
📩 *Order Now:* """ + OWNER_USERNAME + """
📱 *WhatsApp:* """ + OWNER_WHATSAPP + """

⚡ _Limited stock available!_""",

    """⭐ *KPL NISHAD CLOUD SELLER* ⭐
━━━━━━━━━━━━━━━━━━━━

🏆 *Why Choose Us?*

✅ Lowest Prices Guaranteed
✅ 100% Fresh Accounts
✅ Instant Delivery (2 min)
✅ Replacement if any issue
✅ 24/7 Customer Support
✅ 500+ Happy Customers

━━━━━━━━━━━━━━━━━━━━
☁️ *Platforms:*
AWS | Azure | GCP | DigitalOcean

━━━━━━━━━━━━━━━━━━━━
📩 *Owner:* """ + OWNER_USERNAME + """
📱 *WhatsApp:* """ + OWNER_WHATSAPP + """
👨‍💻 *Admin:* """ + ADMIN_USERNAME + """

_Your trusted cloud partner!_""",

    """💎 *PREMIUM CLOUD ACCOUNTS* 💎
━━━━━━━━━━━━━━━━━━━━

🌟 *KPL Cloud Seller - No.1 Trusted Seller*

☁️ *AWS* - Full Console Access
🔵 *Azure* - With Free Credits
🟡 *GCP* - Trial Credits Included
🔷 *DigitalOcean* - With Balance

━━━━━━━━━━━━━━━━━━━━
🎯 *Our Promise:*
• Instant delivery
• Fresh accounts only
• Best market price
• Full support

━━━━━━━━━━━━━━━━━━━━
📩 *DM to Buy:* """ + OWNER_USERNAME + """
📱 *WhatsApp:* """ + OWNER_WHATSAPP + """

_Don't miss out! Order now_ 🚀"""
]

# ═══════════════════════════════════════════
# WELCOME MESSAGE
# ═══════════════════════════════════════════

WELCOME_MSG = """🌐 *Welcome to KPL Cloud Seller!*

━━━━━━━━━━━━━━━━━━━━
☁️ *Premium Cloud Accounts at Best Prices*
━━━━━━━━━━━━━━━━━━━━

We provide premium cloud platform accounts with instant delivery and full support.

☁️ *AWS (Amazon Web Services)*
🔵 *Microsoft Azure*
🟡 *Google Cloud Platform*
🔷 *DigitalOcean*

━━━━━━━━━━━━━━━━━━━━
✅ Instant Delivery
✅ Fresh & Verified Accounts
✅ Best Market Prices
✅ 24/7 Support
✅ Replacement Guarantee
━━━━━━━━━━━━━━━━━━━━

👤 *Owner:* """ + OWNER_USERNAME + """
👨‍💻 *Admin:* """ + ADMIN_USERNAME + """
📱 *WhatsApp:* """ + OWNER_WHATSAPP + """

━━━━━━━━━━━━━━━━━━━━
👇 *Select a platform below to know more:*"""

# ═══════════════════════════════════════════
# PRODUCT DETAILS
# ═══════════════════════════════════════════

PRODUCTS = {
    "aws": {
        "description": """☁️ *AWS (Amazon Web Services) Portal*
━━━━━━━━━━━━━━━━━━━━

✅ Fresh AWS Account
✅ Free Tier Credits Included
✅ Full Console Access
✅ Root Access Available
✅ Instant Delivery (2 min)
✅ Replacement if blocked

━━━━━━━━━━━━━━━━━━━━
💰 *For Price - Contact Owner*

📩 *Owner:* """ + OWNER_USERNAME + """
📱 *WhatsApp:* """ + OWNER_WHATSAPP
    },
    "azure": {
        "description": """🔵 *Microsoft Azure Portal*
━━━━━━━━━━━━━━━━━━━━

✅ Fresh Azure Account
✅ Free Credits Included
✅ Full Portal Access
✅ All Services Enabled
✅ Instant Delivery (2 min)
✅ Replacement if blocked

━━━━━━━━━━━━━━━━━━━━
💰 *For Price - Contact Owner*

📩 *Owner:* """ + OWNER_USERNAME + """
📱 *WhatsApp:* """ + OWNER_WHATSAPP
    },
    "gcloud": {
        "description": """🟡 *Google Cloud Platform (GCP)*
━━━━━━━━━━━━━━━━━━━━

✅ Fresh GCP Account
✅ Free Trial Credits Included
✅ Full Console Access
✅ All APIs Enabled
✅ Instant Delivery (2 min)
✅ Replacement if blocked

━━━━━━━━━━━━━━━━━━━━
💰 *For Price - Contact Owner*

📩 *Owner:* """ + OWNER_USERNAME + """
📱 *WhatsApp:* """ + OWNER_WHATSAPP
    },
    "digitalocean": {
        "description": """🔷 *DigitalOcean*
━━━━━━━━━━━━━━━━━━━━

✅ Fresh DO Account
✅ Free Credits Included
✅ Full Dashboard Access
✅ Droplets & Spaces Access
✅ Instant Delivery (2 min)
✅ Replacement if blocked

━━━━━━━━━━━━━━━━━━━━
💰 *For Price - Contact Owner*

📩 *Owner:* """ + OWNER_USERNAME + """
📱 *WhatsApp:* """ + OWNER_WHATSAPP
    }
}

# ═══════════════════════════════════════════
# BOT HANDLERS
# ═══════════════════════════════════════════

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    keyboard = [
        [InlineKeyboardButton("☁️ AWS", callback_data="aws"),
         InlineKeyboardButton("🔵 Azure", callback_data="azure")],
        [InlineKeyboardButton("🟡 Google Cloud", callback_data="gcloud"),
         InlineKeyboardButton("🔷 DigitalOcean", callback_data="digitalocean")],
        [InlineKeyboardButton("📞 Contact Owner", url="https://t.me/kplboy")],
        [InlineKeyboardButton("📱 WhatsApp", url="https://wa.me/918218829942")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        WELCOME_MSG,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button clicks"""
    query = update.callback_query
    await query.answer()
    
    product_key = query.data
    if product_key in PRODUCTS:
        keyboard = [
            [InlineKeyboardButton("📩 Contact Owner", url="https://t.me/kplboy")],
            [InlineKeyboardButton("📱 WhatsApp", url="https://wa.me/918218829942")],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data="back_to_menu")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            PRODUCTS[product_key]["description"],
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    elif product_key == "back_to_menu":
        keyboard = [
            [InlineKeyboardButton("☁️ AWS", callback_data="aws"),
             InlineKeyboardButton("🔵 Azure", callback_data="azure")],
            [InlineKeyboardButton("🟡 Google Cloud", callback_data="gcloud"),
             InlineKeyboardButton("🔷 DigitalOcean", callback_data="digitalocean")],
            [InlineKeyboardButton("📞 Contact Owner", url="https://t.me/kplboy")],
            [InlineKeyboardButton("📱 WhatsApp", url="https://wa.me/918218829942")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            WELCOME_MSG,
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle any text message"""
    # If message is from a group, save the group ID
    if update.message.chat.type in ["group", "supergroup"]:
        groups = load_groups()
        chat_id = update.message.chat.id
        if chat_id not in groups:
            groups.append(chat_id)
            save_groups(groups)
        return  # Don't reply to every group message
    
    # Only auto-reply in private chats
    keyboard = [
        [InlineKeyboardButton("☁️ AWS", callback_data="aws"),
         InlineKeyboardButton("🔵 Azure", callback_data="azure")],
        [InlineKeyboardButton("🟡 Google Cloud", callback_data="gcloud"),
         InlineKeyboardButton("🔷 DigitalOcean", callback_data="digitalocean")],
        [InlineKeyboardButton("📞 Contact Owner", url="https://t.me/kplboy")],
        [InlineKeyboardButton("📱 WhatsApp", url="https://wa.me/918218829942")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 *Hello!*\n\nWelcome to KPL Cloud Seller. Select a platform below or type /start for full menu:\n\n📩 *Owner:* " + OWNER_USERNAME + "\n📱 *WhatsApp:* " + OWNER_WHATSAPP,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def track_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Track when bot is added to a group"""
    if update.my_chat_member:
        chat = update.my_chat_member.chat
        new_status = update.my_chat_member.new_chat_member.status
        
        if chat.type in ["group", "supergroup"]:
            groups = load_groups()
            if new_status in ["member", "administrator"]:
                if chat.id not in groups:
                    groups.append(chat.id)
                    save_groups(groups)
                    logging.info(f"✅ Added to group: {chat.title} ({chat.id})")
            elif new_status in ["left", "kicked"]:
                if chat.id in groups:
                    groups.remove(chat.id)
                    save_groups(groups)
                    logging.info(f"❌ Removed from group: {chat.title} ({chat.id})")

async def send_promo_to_groups(context: ContextTypes.DEFAULT_TYPE):
    """Send promotional message to all groups"""
    groups = load_groups()
    if not groups:
        logging.info("No groups to send promo to.")
        return
    
    promo = random.choice(PROMO_MESSAGES)
    
    keyboard = [
        [InlineKeyboardButton("📩 Order Now", url="https://t.me/kplboy")],
        [InlineKeyboardButton("📱 WhatsApp", url="https://wa.me/918218829942")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    sent_count = 0
    for group_id in groups.copy():
        try:
            await context.bot.send_message(
                chat_id=group_id,
                text=promo,
                parse_mode="Markdown",
                reply_markup=reply_markup
            )
            sent_count += 1
            logging.info(f"✅ Promo sent to group: {group_id}")
        except Exception as e:
            logging.error(f"❌ Failed to send to {group_id}: {e}")
            if "Forbidden" in str(e) or "Chat not found" in str(e):
                groups.remove(group_id)
                save_groups(groups)
        await asyncio.sleep(1)  # Rate limiting
    
    logging.info(f"📢 Promo sent to {sent_count}/{len(groups)} groups")

# ═══════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════

def main():
    """Start the bot"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_handler(ChatMemberHandler(track_group, ChatMemberHandler.MY_CHAT_MEMBER))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Schedule promo messages - 4 times daily (IST)
    # Subah 9:00 AM IST = 3:30 UTC
    # Dopahar 1:00 PM IST = 7:30 UTC
    # Sham 6:00 PM IST = 12:30 UTC
    # Raat 9:30 PM IST = 16:00 UTC
    job_queue = app.job_queue
    job_queue.run_daily(send_promo_to_groups, time=time(hour=3, minute=30))   # 9:00 AM IST
    job_queue.run_daily(send_promo_to_groups, time=time(hour=7, minute=30))   # 1:00 PM IST
    job_queue.run_daily(send_promo_to_groups, time=time(hour=12, minute=30))  # 6:00 PM IST
    job_queue.run_daily(send_promo_to_groups, time=time(hour=16, minute=0))   # 9:30 PM IST
    
    print("═══════════════════════════════════════════")
    print("🤖 KPL Cloud Seller Bot is RUNNING!")
    print("═══════════════════════════════════════════")
    print(f"👤 Owner: {OWNER_USERNAME}")
    print(f"👨‍💻 Admin: {ADMIN_USERNAME}")
    print(f"📱 WhatsApp: {OWNER_WHATSAPP}")
    print("═══════════════════════════════════════════")
    print("📢 Promo Schedule (IST):")
    print("   • 9:00 AM  - Morning")
    print("   • 1:00 PM  - Afternoon")
    print("   • 6:00 PM  - Evening")
    print("   • 9:30 PM  - Night")
    print("═══════════════════════════════════════════")
    
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
