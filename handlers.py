from telegram import Update
from telegram.ext import ContextTypes

from config import (
    CHANNEL,
    DAILY_REWARD,
    INVITE_REWARD,
)
from keyboards import (
    join_keyboard,
    main_menu,
    shop_menu,
)
from database import (
    add_user,
    get_coins,
    add_coins,
    get_daily,
    set_daily,
)

from datetime import date


async def is_joined(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in [
            "member",
            "administrator",
            "creator",
        ]
    except Exception:
        return False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await add_user(
        user.id,
        user.first_name,
        user.username,
    )

    if not await is_joined(context.bot, user.id):
        await update.message.reply_text(
            "👋 برای استفاده از ربات ابتدا عضو کانال شو.",
            reply_markup=join_keyboard(),
        )
        return

    await update.message.reply_text(
        f"سلام {user.first_name} 🌸\n\nبه ربات سنسیویتی خوش اومدی.",
        reply_markup=main_menu(),
    )
    async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user.id

    if query.data == "check_join":

        if await is_joined(context.bot, user):
            await query.message.edit_text(
                "✅ عضویت شما تایید شد.",
                reply_markup=main_menu(),
            )
        else:
            await query.answer(
                "❌ هنوز عضو کانال نیستی.",
                show_alert=True,
            )

    elif query.data == "menu":
        await query.message.edit_text(
            "🏠 منوی اصلی",
            reply_markup=main_menu(),
        )

    elif query.data == "coins":
        coins = await get_coins(user)

        await query.answer(
            f"🪙 موجودی شما: {coins}",
            show_alert=True,
        )

    elif query.data == "profile":
        coins = await get_coins(user)

        await query.message.edit_text(
            f"""👤 پروفایل

🆔 شناسه: {user}
🪙 سکه: {coins}
""",
            reply_markup=main_menu(),
        )

    elif query.data == "shop":
        await query.message.edit_text(
            "🛒 فروشگاه سنسیویتی",
            reply_markup=shop_menu(),
        )

    elif query.data == "invite":
        link = f"https://t.me/{context.bot.username}?start={user}"

        await query.message.edit_text(
            f"""👥 دعوت دوستان

لینک اختصاصی شما:

{link}

🎁 به ازای هر دعوت موفق:
+{INVITE_REWARD} سکه
""",
            reply_markup=main_menu(),
        )

    elif query.data == "daily":
        today = str(date.today())
        last = await get_daily(user)

        if last == today:
            await query.answer(
                "⏳ جایزه امروز را قبلاً دریافت کرده‌ای.",
                show_alert=True,
            )
        else:
            await add_coins(user, DAILY_REWARD)
            await set_daily(user, today)

            await query.answer(
                f"🎉 {DAILY_REWARD} سکه دریافت کردی
