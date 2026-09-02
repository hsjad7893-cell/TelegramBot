from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import TOKEN
from database import create_db
from handlers import start, check_join
from admin import admin_panel, stats, broadcast, handle_broadcast


async def post_init(app: Application):
    await create_db()


def main():
    app = (
        Application.builder()
        .token(TOKEN)
        .post_init(post_init)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin_panel))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CallbackQueryHandler(check_join, pattern="check_join"))
    app.add_handler(MessageHandler(filters.ALL, handle_broadcast))

    print("🤖 Bot Started")
    app.run_polling()

if __name__ == "__main__":
    main()
