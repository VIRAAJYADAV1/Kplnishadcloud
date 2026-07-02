import asyncio
import logging
import json
import os
import random
from datetime import time

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# ═══════════════════════════════════════════
# KPL CLOUD SELLER BOT
# Owner: @kplboy
# Admin: @VIRAAJYADAV_247
# ═══════════════════════════════════════════

BOT_TOKEN = "8520478105:AAHmcF-PYvIvuq_5IqQudpdeqeTJOg1cczE"

OWNER_USERNAME = "@kplboy"
OWNER_WHATSAPP = "+91 82188 29942"
ADMIN_USERNAME = "@VIRAAJYADAV_247"

GROUPS_FILE = "groups.json"


def load_groups():
    try:
        if os.path.exists(GROUPS_FILE):
            with open(GROUPS_FILE, "r") as f:
                return json.load(f)
    except Exception:
        pass
    return []


def save_groups(groups):
    try:
        with open(GROUPS_FILE, "w") as f:
            json.dump(groups, f)
    except Exception:
        pass


# ═══════════════════════════════════════════
# MESSAGES
# ═══════════════════════════════════════════

WELCOME_MSG = (
    "🌐 *Welcome to KPL Cloud Seller!*\n"
    "\n"
    "━━━━━━━━━━━━━━━━━━━━\n"
    "☁️ *Premium Cloud Accounts at Best Prices*\n"
    "━━━━━━━━━━━━━━━━━━━━\n"
    "\n"
    "We provide premium cloud platform accounts:\n"
    "\n"
    "☁️ *AWS (Amazon Web Services)*\n"
    "🔵 *Microsoft Azure*\n"
    "🟡 *Google Cloud Platform*\n"
    "🔷 *DigitalOcean*\n"
    "\n"
    "━━━━━━━━━━━━━━━━━━━━\n"
    "✅ Instant Delivery\n"
    "✅ Fresh & Verified Accounts\n"
    "✅ Best Market Prices\n"
    "✅ 24/7 Support\n"
    "✅ Replacement Guarantee\n"
    "━━━━━━━━━━━━━━━━━━━━\n"
    "\n"
    "👤 *Owner:* @kplboy\n"
    "👨‍💻 *Admin:* @VIRAAJYADAV_247\n"
    "📱 *WhatsApp:* +91 82188 29942\n"
    "\n"
    "━━━━━━━━━━━━━━━━━━━━\n"
    "👇 *Select a platform below:*"
)

PROMO_MESSAGES = [
    (
        "🌐 *KPL CLOUD SELLER* 🌐\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "\n"
        "☁️ *Premium Cloud Accounts Available!*\n"
        "\n"
        "☁️ AWS (Amazon Web Services)\n"
        "🔵 Microsoft Azure Portal\n"
        "🟡 Google Cloud Platform (GCP)\n"
        "🔷 DigitalOcean\n"
        "\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💰 *Best Prices in Market*\n"
        "⚡ *Instant Delivery*\n"
        "🛡️ *100% Trusted*\n"
        "🔄 *Replacement Guarantee*\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "\n"
        "📩 *Owner:* @kplboy\n"
        "📱 *WhatsApp:* +91 82188 29942\n"
        "\n"
        "_DM now to get your cloud account!_"
    ),
    (
        "🔥 *FLASH SALE - CLOUD ACCOUNTS* 🔥\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "\n"
        "🚀 *Available Platforms:*\n"
        "\n"
        "1️⃣ ☁️ AWS Portal\n"
        "2️⃣ 🔵 Azure Portal\n"
        "3️⃣ 🟡 Google Cloud\n"
        "4️⃣ 🔷 DigitalOcean\n"
        "\n"
        "✅ Fresh & Verified Accounts\n"
        "✅ With Free Credits\n"
        "✅ Full Access\n"
        "✅ Instant Delivery\n"
        "✅ After-Sale Support\n"
        "\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📩 *Order Now:* @kplboy\n"
        "📱 *WhatsApp:* +91 82188 29942\n"
        "\n"
        "⚡ _Limited stock available!_"
    ),
    (
        "⭐ *KPL NISHAD CLOUD SELLER* ⭐\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "\n"
        "🏆 *Why Choose Us?*\n"
        "\n"
        "✅ Lowest Prices Guaranteed\n"
        "✅ 100% Fresh Accounts\n"
        "✅ Instant Delivery (2 min)\n"
        "✅ Replacement if any issue\n"
        "✅ 24/7 Customer Support\n"
        "✅ 500+ Happy Customers\n"
        "\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "☁️ *Platforms:*\n"
        "AWS | Azure | GCP | DigitalOcean\n"
        "\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📩 *Owner:* @kplboy\n"
        "📱 *WhatsApp:* +91 82188 29942\n"
        "👨‍💻 *Admin:* @VIRAAJYADAV_247\n"
        "\n"
        "_Your trusted cloud partner!_"
    ),
    (
        "💎 *PREMIUM CLOUD ACCOUNTS* 💎\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "\n"
        "🌟 *KPL Cloud Seller - No.1 Trusted Seller*\n"
        "\n"
        "☁️ *AWS* - Full Console Access\n"
        "🔵 *Azure* - With Free Credits\n"
        "🟡 *GCP* - Trial Credits Included\n"
        "🔷 *DigitalOcean* - With Balance\n"
        "\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎯 *Our Promise:*\n"
        "• Instant delivery\n"
        "• Fresh accounts only\n"
        "• Best market price\n"
        "• Full support\n"
        "\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📩 *DM to Buy:* @kplboy\n"
        "📱 *WhatsApp:* +91 82188 29942\n"
        "\n"
        "_Don't miss out! Order now_ 🚀"
    ),
]

PRODUCTS = {
    "aws": (
        "☁️ *AWS (Amazon Web Services) Portal*\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "\n"
        "✅ Fresh AWS Account\n"
        "✅ Free Tier Credits Included\n"
        "✅ Full Console Access\n"
        "✅ Root Access Available\n"
        "✅ Instant Delivery (2 min)\n"
        "✅ Replacement if blocked\n"
        "\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💰 *For Price - Contact Owner*\n"
        "\n"
        "📩 *Owner:* @kplboy\n"
        "📱 *WhatsApp:* +91 82188 29942"
    ),
    "azure": (
        "🔵 *Microsoft Azure Portal*\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "\n"
        "✅ Fresh Azure Account\n"
        "✅ Free Credits Included\n"
        "✅ Full Portal Access\n"
        "✅ All Services Enabled\n"
        "✅ Instant Delivery (2 min)\n"
        "✅ Replacement if blocked\n"
        "\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💰 *For Price - Contact Owner*\n"
        "\n"
        "📩 *Owner:* @kplboy\n"
        "📱 *WhatsApp:* +91 82188 29942"
    ),
    "gcloud": (
        "🟡 *Google Cloud Platform (GCP)*\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "\n"
        "✅ Fresh GCP Account\n"
        "✅ Free Trial Credits Included\n"
        "✅ Full Console Access\n"
        "✅ All APIs Enabled\n"
        "✅ Instant Delivery (2 min)\n"
        "✅ Replacement if blocked\n"
        "\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💰 *For Price - Contact Owner*\n"
        "\n"
        "📩 *Owner:* @kplboy\n"
        "📱 *WhatsApp:* +91 82188 29942"
    ),
    "digitalocean": (
        "🔷 *DigitalOcean*\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "\n"
        "✅ Fresh DO Account\n"
        "✅ Free Credits Included\n"
        "✅ Full Dashboard Access\n"
        "✅ Droplets & Spaces Access\n"
        "✅ Instant Delivery (2 min)\n"
        "✅ Replacement if blocked\n"
        "\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💰 *For Price - Contact Owner*\n"
        "\n"
        "📩 *Owner:* @kplboy\n"
        "📱 *WhatsApp:* +91 82188 29942"
    ),
}


# ═══════════════════════════════════════════
# KEYBOARDS
# ═══════════════════════════════════════════

def main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("☁️ AWS", callback_data="aws"),
         InlineKeyboardButton("🔵 Azure", callback_data="azure")],
        [InlineKeyboardButton("🟡 Google Cloud", callback_data="gcloud"),
         InlineKeyboardButton("🔷 DigitalOcean", callback_data="digitalocean")],
        [InlineKeyboardButton("📞 Contact Owner", url="https://t.me/kplboy")],
        [InlineKeyboardButton("📱 WhatsApp", url="https://wa.me/918218829942")],
    ])


def product_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📩 Contact Owner", url="https://t.me/kplboy")],
        [InlineKeyboardButton("📱 WhatsApp", url="https://wa.me/918218829942")],
        [InlineKeyboardButton("🔙 Back to Menu", callback_data="back_to_menu")],
    ])


def promo_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📩 Order Now", url="https://t.me/kplboy")],
        [InlineKeyboardButton("📱 WhatsApp", url="https://wa.me/918218829942")],
    ])


# ═══════════════════════════════════════════
# HANDLERS
# ═══════════════════════════════════════════

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    try:
        if update.message:
            # Track group
            if update.message.chat.type in ["group", "supergroup"]:
                groups = load_groups()
                chat_id = update.message.chat.id
                if chat_id not in groups:
                    groups.append(chat_id)
                    save_groups(groups)

            await update.message.reply_text(
                WELCOME_MSG,
                parse_mode="Markdown",
                reply_markup=main_keyboard(),
            )
    except Exception as e:
        logging.error(f"Error in start_command: {e}")


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button clicks"""
    try:
        query = update.callback_query
        if not query:
            return
        await query.answer()

        data = query.data

        if data in PRODUCTS:
            await query.edit_message_text(
                PRODUCTS[data],
                parse_mode="Markdown",
                reply_markup=product_keyboard(),
            )
        elif data == "back_to_menu":
            await query.edit_message_text(
                WELCOME_MSG,
                parse_mode="Markdown",
                reply_markup=main_keyboard(),
            )
    except Exception as e:
        logging.error(f"Error in button_callback: {e}")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle any text message"""
    try:
        if not update.message:
            return

        chat = update.message.chat

        # Track groups
        if chat.type in ["group", "supergroup"]:
            groups = load_groups()
            if chat.id not in groups:
                groups.append(chat.id)
                save_groups(groups)
            return  # Don't reply in groups

        # Auto-reply in private chats only
        await update.message.reply_text(
            "👋 *Hello!*\n\nWelcome to KPL Cloud Seller.\nSelect a platform below or type /start\n\n"
            "📩 *Owner:* @kplboy\n"
            "📱 *WhatsApp:* +91 82188 29942",
            parse_mode="Markdown",
            reply_markup=main_keyboard(),
        )
    except Exception as e:
        logging.error(f"Error in handle_message: {e}")


async def send_promo_to_groups(context: ContextTypes.DEFAULT_TYPE):
    """Send promotional message to all saved groups"""
    groups = load_groups()
    if not groups:
        logging.info("No groups to send promo.")
        return

    promo = random.choice(PROMO_MESSAGES)

    for group_id in groups.copy():
        try:
            await context.bot.send_message(
                chat_id=group_id,
                text=promo,
                parse_mode="Markdown",
                reply_markup=promo_keyboard(),
            )
            logging.info(f"Promo sent to: {group_id}")
        except Exception as e:
            logging.error(f"Failed to send to {group_id}: {e}")
            if "Forbidden" in str(e) or "not found" in str(e):
                groups.remove(group_id)
                save_groups(groups)
        await asyncio.sleep(1)


# ═══════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    app = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_message))

    # Schedule 4 daily promos (IST times)
    job_queue = app.job_queue
    if job_queue:
        job_queue.run_daily(send_promo_to_groups, time=time(hour=3, minute=30))   # 9:00 AM IST
        job_queue.run_daily(send_promo_to_groups, time=time(hour=7, minute=30))   # 1:00 PM IST
        job_queue.run_daily(send_promo_to_groups, time=time(hour=12, minute=30))  # 6:00 PM IST
        job_queue.run_daily(send_promo_to_groups, time=time(hour=16, minute=0))   # 9:30 PM IST
        logging.info("Promo schedule: 9AM, 1PM, 6PM, 9:30PM IST")

    print("═══════════════════════════════════════════")
    print("🤖 KPL Cloud Seller Bot is RUNNING!")
    print("═══════════════════════════════════════════")
    print(f"👤 Owner: {OWNER_USERNAME}")
    print(f"👨‍💻 Admin: {ADMIN_USERNAME}")
    print(f"📱 WhatsApp: {OWNER_WHATSAPP}")
    print("═══════════════════════════════════════════")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
