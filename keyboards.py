from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def join_keyboard():
    keyboard = [
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
    ]
    return InlineKeyboardMarkup(keyboard)


def main_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🪙 موجودی سکه",
                callback_data="coins"
            )
        ],
        [
            InlineKeyboardButton(
                "🎮 خرید سنسیویتی",
                callback_data="shop"
            )
        ],
        [
            InlineKeyboardButton(
                "👥 دعوت دوستان",
                callback_data="invite"
            )
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def shop_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🔥 هدشات (20🪙)",
                callback_data="buy_headshot"
            )
        ],
        [
            InlineKeyboardButton(
                "📱 آیفون (30🪙)",
                callback_data="buy_iphone"
            )
        ],
        [
            InlineKeyboardButton(
                "🤖 سامسونگ (30🪙)",
                callback_data="buy_samsung"
            )
        ],
        [
            InlineKeyboardButton(
                "🎯 HUD (40🪙)",
                callback_data="buy_hud"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="menu"
            )
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
