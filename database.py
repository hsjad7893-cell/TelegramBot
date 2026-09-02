import aiosqlite

DB_NAME = "bot.db"


async def create_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            username TEXT,
            coins INTEGER DEFAULT 50,
            invited_by INTEGER DEFAULT 0,
            last_daily TEXT DEFAULT ""
        )
        """)
        await db.commit()


async def add_user(user_id, first_name, username):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            """
            INSERT OR IGNORE INTO users(user_id, first_name, username)
            VALUES(?,?,?)
            """,
            (user_id, first_name, username),
        )
        await db.commit()


async def get_user(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cur = await db.execute(
            "SELECT * FROM users WHERE user_id=?",
            (user_id,),
        )
        return await cur.fetchone()


async def get_coins(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cur = await db.execute(
            "SELECT coins FROM users WHERE user_id=?",
            (user_id,),
        )
        row = await cur.fetchone()
        return row[0] if row else 0


async def add_coins(user_id, amount):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE users SET coins = coins + ? WHERE user_id=?",
            (amount, user_id),
        )
        await db.commit()


async def remove_coins(user_id, amount):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE users SET coins = coins - ? WHERE user_id=?",
            (amount, user_id),
        )
        await db.commit()


async def set_daily(user_id, date):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE users SET last_daily=? WHERE user_id=?",
            (date, user_id),
        )
        await db.commit()


async def get_daily(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cur = await db.execute(
            "SELECT last_daily FROM users WHERE user_id=?",
            (user_id,),
        )
        row = await cur.fetchone()
        return row[0] if row else ""


async def users_count():
    async with aiosqlite.connect(DB_NAME) as db:
        cur = await db.execute("SELECT COUNT(*) FROM users")
        row = await cur.fetchone()
        return row[0]


async
