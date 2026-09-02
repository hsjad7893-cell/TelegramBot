from datetime import datetime

from telegram import Update
from telegram.ext import ContextTypes

from config import (
    CHANNEL,
    DAILY_REWARD,
    INVITE_REWARD,
    SHOP,
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
    remove_coins,
    get_daily,
    set_daily,
)


async def is_joined(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in [
            "member",
            "administrator",
            "creator",
        ]
    except:
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
            "❌ ابتدا در کانال عضو شو.",
            reply_markup=join_keyboard(),
        )
        return

    await update.message.reply_text(
        f"""🎮 سلام {user.first_name}

به ربات سنسیویتی خوش اومدی.
از منوی زیر استفاده کن 👇
""",
        reply_markup=main_menu(),
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    user = query.from_user.id

    if query.data == "check_join":

        if await is_joined(context.bot, user):

            await query.message.edit_text(
                "✅ عضویت تایید شد.",
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

    elif query.data == " 
        elif query.data == "invite":

        link = f"https://t.me/{context.bot.username}?start={user}"

        await query.message.edit_text(
            f"""👥 دعوت دوستان

لینک دعوت اختصاصی شما:

{link}

🎁 به ازای هر نفر:
+{INVITE_REWARD} سکه
""",
            reply_markup=main_menu(),
        )

    elif query.data == "help":

        await query.message.edit_text(
            """ℹ️ راهنما

🪙 با دعوت دوستان سکه بگیر.
🎁 هر روز جایزه دریافت کن.
🛒 با سکه سنسیویتی بخر.
""",
            reply_markup=main_menu(),
        )

    elif query.data.startswith("buy_"):

        item = query.data.replace("buy_", "")

        product = SHOP[item]

        coins = await get_coins(user)

        if coins < product["price"]:

            await query.answer(
                "❌ سکه کافی نداری.",
                show_alert=True,
            )

            return

        await remove_coins(
            user,
            product["price"],
        )

        coins = await get_coins(user)

        await query.message.edit_text(
            f"""✅ خرید انجام شد.

📦 {product["name"]}

{product["text"]}

🪙 موجودی باقی‌مانده:
{coins}
""",
            reply_markup=main_menu(),
        )
