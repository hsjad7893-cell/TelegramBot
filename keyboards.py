from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import CHANNEL

def join_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "📢 عضویت در کانال",
                url=f"https://t.me/{CHANNEL.replace('@','')}"
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

def admin_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("📊 آمار کاربران", callback_data="stats")
        ],
        [
            InlineKeyboardButton("📢 ارسال همگانی", callback_data="broadcast")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
