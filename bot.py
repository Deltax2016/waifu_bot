from aiogram import Dispatcher, Bot, types
from random import random

TOKEN = "1989718665:AAFCneR0UwDLssi6ONAVaXAYXHgMZR0P-94"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

phrases = ["Привет, очень рада тебя видеть ", "Приветик, меня зовут Наташа, познакомимся? Я люблю читать мангу и смотреть аниме, а ты ", "Ой, привет, расскажи о себе "]


@dp.message_handler(commands="start")
async def start(message: types.Message):
    file_db = open('./notifications/fake_db.py')
    db = eval(file_db.read())
    file_db.close()
    db[message.from_user.id] = {"stage": 0}
    file_db = open('./notifications/fake_db.py','w')
    file_db.write(str(db))
    text = random.choice(phrases)
    await message.answer(f"{text}{message.from_user.first_name}")

@dp.message_handler(commands="stop")
async def stop(message: types.Message):
    file_db = open('./notifications/fake_db.py')
    db = eval(file_db.read())
    file_db.close()
    db[message.from_user.id] = {"notifications": "no"}
    file_db = open('./notifications/fake_db.py','w')
    file_db.write(str(db))
    await message.answer(f"Notifications stopped")

    return "ok"