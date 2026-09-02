from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def join_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📢 عضویت در کانال",
                url="https://t.me/GUILD_ALCATRAZ"
            )
        ],
        [
            InlineKeyboardButton(
                "✅ عضو شدم",
                callback_data="check_join"
            )
        ]
    ])


def main_menu():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "👤 پروفایل",
                callback_data="profile"
            ),
            InlineKeyboardButton(
                "🪙 موجودی",
                callback_data="coins"
            )
        ],
        [
            InlineKeyboardButton(
                "🎁 جایزه روزانه",
                callback_data="daily"
            ),
            InlineKeyboardButton(
                "👥 دعوت دوستان",
                callback_data="invite"
            )
        ],
        [
            InlineKeyboardButton(
                "🛒 فروشگاه",
                callback_data="shop"
            )
        ],
        [
            InlineKeyboardButton(
                "ℹ️ راهنما",
                callback_data="help"
            )
        ]
    ])


def shop_menu():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🔥 Headshot Pro - 20🪙",
                callback_data="buy_headshot"
            )
        ],
        [
            InlineKeyboardButton(
                "🤖 Android Smooth - 25🪙",
                callback_data="buy_android"
            )
        ],
        [
            InlineKeyboardButton(
                "🍎 iPhone Zero Recoil - 30🪙",
                callback_data="buy_iphone"
            )
        ],
        [
            InlineKeyboardButton(
                "🎯 HUD Pack - 40🪙",
                callback_data="buy_hud"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="menu"
            )
        ]
    ])
