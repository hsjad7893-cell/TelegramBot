from telegram.ext import (
    Application,
    CommandHandler,
)

from config import TOKEN
from database import create_db
from handlers import start


async def post_init(app: Application):
    await create_db()


app = Application.builder().token(TOKEN).post_init(post_init).build()

app.add_handler(CommandHandler("start", start))

print("🤖 Bot Started...")

app.run_polling()
