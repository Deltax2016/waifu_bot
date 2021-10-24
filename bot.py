from aiogram import Dispatcher, Bot, types
from random import *
import requests
from googletrans import Translator

TOKEN = "1989718665:AAFCneR0UwDLssi6ONAVaXAYXHgMZR0P-94"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

phrases = ["Привет, очень рада тебя видеть ", "Приветик, меня зовут Наташа, познакомимся? Я люблю читать мангу и смотреть аниме, а ты ", "Ой, привет, расскажи о себе "]




@dp.message_handler(commands="start")
async def start(message: types.Message):
    file_db = open('./fake_db.py')
    db = eval(file_db.read())
    file_db.close()
    db[message.from_user.id] = {"stage": 0}
    file_db = open('./fake_db.py','w')
    file_db.write(str(db))
    text = choice(phrases)
    await message.answer(f"{text}{message.from_user.first_name}")

@dp.message_handler(commands="stop")
async def stop(message: types.Message):
    file_db = open('./fake_db.py')
    db = eval(file_db.read())
    file_db.close()
    db[message.from_user.id] = {"stage": 10}
    file_db = open('./fake_db.py','w')
    file_db.write(str(db))
    await message.answer(f"Notifications stopped")

    return "ok"

@dp.message_handler()
async def start(message: types.Message):
    s = ""
    if "историю про" in message.text:
        s = message.text.split("про ")[1]
        print("hey")
        await bot.send_message(message.from_user.id, "Подожди немного, я подумаю")

    query = {
          "option": "Hero Story Villian",
          "main_field_value": message.from_user.id,
          "secondary_field_value": s,
          "tone": "Empathetic"
        }
    r = requests.post("http://212.193.50.2:777/two_field_tools", json=query)
    kek = r.json()['texts'][0]
    translator = Translator()
    translations = translator.translate([kek], dest='ru')
    
    await message.answer(translations[0].text)









