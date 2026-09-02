from telegram import Update
from telegram.ext import ContextTypes
from config import ADMINS
from database import users_count

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMINS:
        return

    count = await users_count()

    await update.message.reply_text(
        f"""👑 پنل مدیریت

👥 تعداد کاربران: {count}

دستورها:
/stats - آمار
/broadcast - ارسال همگانی (بعداً اضافه می‌شود)
"""
    )

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMINS:
        return

    count = await users_count()

    await update.message.reply_text(
        f"📊 تعداد کاربران ربات: {count}"
    )
from database import get_all_users

broadcast_mode = {}

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMINS:
        return

    broadcast_mode[update.effective_user.id] = True
    await update.message.reply_text("📢 پیام همگانی را ارسال کن.")

async def handle_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in broadcast_mode:
        return

    users = await get_all_users()

    ok = 0

    for user in users:
        try:
            await context.bot.copy_message(
                chat_id=user[0],
                from_chat_id=update.effective_chat.id,
                message_id=update.message.message_id
            )
            ok += 1
        except:
            pass

    del broadcast_mode[update.effective_user.id]

    await update.message.reply_text(f"✅ برای {ok} نفر ارسال شد.")
