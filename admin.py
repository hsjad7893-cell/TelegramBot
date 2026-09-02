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
