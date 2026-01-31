import os
import random
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

users = {}

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user_id = message.from_user.id

    if user_id not in users:
        users[user_id] = {
            "team": "Безымянные",
            "money": 1000,
            "rating": 50
        }

    await message.answer(
        "⚽ Добро пожаловать в футбольный менеджер!\n\n"
        "Команды:\n"
        "/team — моя команда\n"
        "/match — сыграть матч"
    )


@dp.message_handler(commands=["team"])
async def team(message: types.Message):
    user = users[message.from_user.id]

    text = (
        f"🏟 Команда: {user['team']}\n"
        f"💰 Деньги: {user['money']}\n"
        f"⭐ Рейтинг: {user['rating']}"
    )

    await message.answer(text)


@dp.message_handler(commands=["match"])
async def match(message: types.Message):
    user = users[message.from_user.id]

    enemy = random.randint(30, 70)
    my_power = user["rating"] + random.randint(-10, 10)

    if my_power > enemy:
        reward = random.randint(100, 300)
        user["money"] += reward
        user["rating"] += 1
        await message.answer(f"✅ Победа!\nТы заработал {reward}$")
    else:
        await message.answer("❌ Поражение...")


if __name__ == "__main__":
    executor.start_polling(dp)
      
