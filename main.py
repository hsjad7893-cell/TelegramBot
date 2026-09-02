from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from config import TOKEN
from database import create_db
from handlers import start, buttons


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

    app.add_handler(
        CallbackQueryHandler(buttons)
    )

    print("Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
