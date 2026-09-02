from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

CHANNEL = "@GUILD_ALCATRAZ"

ADMINS = [8999545910]

# پاداش‌ها
START_COINS = 50
DAILY_REWARD = 10
INVITE_REWARD = 15

# قیمت محصولات
SHOP = {
    "headshot": {
        "name": "🔥 Headshot Pro",
        "price": 20,
        "text": """🔥 Headshot Pro

General : 200
Red Dot : 180
2X Scope : 170
4X Scope : 160
Sniper : 20
Free Look : 50
"""
    },

    "android": {
        "name": "🤖 Android Smooth",
        "price": 25,
        "text": """🤖 Android Smooth

General : 190
Red Dot : 175
2X : 165
4X : 155
AWM : 10
"""
    },

    "iphone": {
        "name": "🍎 iPhone Zero Recoil",
        "price": 30,
        "text": """🍎 iPhone

General : 195
Red Dot : 185
2X : 175
4X : 165
Sniper : 0
"""
    },

    "hud": {
        "name": "🎯 HUD Pack",
        "price": 40,
        "text": """🎯 HUD حرفه‌ای

4 Finger HUD
Drag Headshot
Fast Scope
"""
    }
}
