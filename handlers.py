from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatMemberStatus

from config import CHANNEL
from keyboards import join_keyboard, main_menu
from database import add_user


async def is_joined(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)

        return member.status in [
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ]
    except:
        return False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    await add_user(
        user.id,
        user.first_name,
        user.username
    )

    if not await is_joined(context.bot, user.id):

        await update.message.reply_text(
            "🔒 برای استفاده از ربات ابتدا عضو کانال شوید.",
            reply_markup=join_keyboard()
        )

        return

    await update.message.reply_text(
        f"""
🎉 سلام {user.first_name}

به ربات Free Fire Coin خوش آمدی.

از منوی زیر استفاده کن.
""",
        reply_markup=main_menu()
    )
