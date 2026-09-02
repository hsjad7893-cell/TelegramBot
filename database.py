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
            invited_by INTEGER DEFAULT 0
        )
        """)

        await db.commit()


async def add_user(user_id, first_name, username):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            """
            INSERT OR IGNORE INTO users
            (user_id, first_name, username)
            VALUES(?,?,?)
            """,
            (user_id, first_name, username)
        )
        await db.commit()


async def get_user(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cur = await db.execute(
            "SELECT * FROM users WHERE user_id=?",
            (user_id,)
        )
        return await cur.fetchone()


async def get_coins(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cur = await db.execute(
            "SELECT coins FROM users WHERE user_id=?",
            (user_id,)
        )
        row = await cur.fetchone()

        if row:
            return row[0]

        return 0


async def add_coins(user_id, amount):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE users SET coins=coins+? WHERE user_id=?",
            (amount, user_id)
        )
        await db.commit()


async def remove_coins(user_id, amount):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE users SET coins=coins-? WHERE user_id=?",
            (amount, user_id)
        )
        await db.commit()


async def users_count():
    async with aiosqlite.connect(DB_NAME) as db:
        cur = await db.execute(
            "SELECT COUNT(*) FROM users"
        )
        row = await cur.fetchone()
        return row[0]


async def get_all_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cur = await db.execute(
            "SELECT user_id FROM users"
        )
        return await cur.fetchall()
