from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatMemberStatus

from config import CHANNEL
from database import add_user
from keyboards import join_keyboard

async def check_member(bot, user_id):
    member = await bot.get_chat_member(CHANNEL, user_id)
    return member.status in (
        ChatMemberStatus.MEMBER,
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.OWNER,
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await add_user(
        user.id,
        user.first_name or "",
        user.username or ""
    )

    if not await check_member(context.bot, user.id):
        await update.message.reply_text(
            "❌ برای استفاده از ربات ابتدا عضو کانال شوید.",
            reply_markup=join_keyboard()
        )
        return

    await update.message.reply_text(
        f"سلام {user.first_name} 👋\n\n"
        "✅ عضویت شما تایید شد.\n"
        "به ربات خوش آمدید."
    )
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def check_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user

    if await check_member(context.bot, user.id):
        await query.edit_message_text(
            f"🎉 سلام {user.first_name}\n\nعضویت شما تایید شد."
        )
    else:
        await query.answer(
            "❌ هنوز عضو کانال نیستی.",
            show_alert=True
        )
app.add_handler(CommandHandler("broadcast", broadcast))
app.add_handler(MessageHandler(filters.ALL, handle_broadcast))
