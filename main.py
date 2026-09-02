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
from telegram.ext import CallbackQueryHandler
app.add_handler(CommandHandler("start", start))
from handlers import check_join

app.add_handler(CallbackQueryHandler(check_join, pattern="check_join"))
from admin import admin_panel, stats
app.add_handler(CommandHandler("admin", admin_panel))
app.add_handler(CommandHandler("stats", stats))
from telegram.ext import CallbackQueryHandler
from handlers import check_join
from admin import admin_panel, stats
app.add_handler(CommandHandler("admin", admin_panel))
app.add_handler(CommandHandler("stats", stats))
app.add_handler(CallbackQueryHandler(check_join, pattern="check_join"))
from admin import broadcast, handle_broadcast
from telegram.ext import MessageHandler, filters
