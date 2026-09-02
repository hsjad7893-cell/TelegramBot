import aiosqlite

DB_NAME = "bot.db"

async def create_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            username TEXT
        )
        """)
        await db.commit()

async def add_user(user_id, first_name, username):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users(user_id, first_name, username) VALUES(?,?,?)",
            (user_id, first_name, username)
        )
        await db.commit()

async def get_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT user_id FROM users")
        users = await cursor.fetchall()
        return users

async def users_count():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT COUNT(*) FROM users")
        count = await cursor.fetchone()
        return count[0]
async def get_all_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT user_id FROM users")
        return await cursor.fetchall()
import aiosqlite

DB = "bot.db"

async def add_coins(user_id, amount):
    async with aiosqlite.connect(DB) as db:
        await db.execute(
            "UPDATE users SET coins = coins + ? WHERE user_id=?",
            (amount, user_id),
        )
        await db.commit()


async def get_coins(user_id):
    async with aiosqlite.connect(DB) as db:
        cur = await db.execute(
            "SELECT coins FROM users WHERE user_id=?",
            (user_id,),
        )
        row = await cur.fetchone()
        return row[0] if row else 0
