from fastapi import FastAPI
from bot import TOKEN, dp, bot
from aiogram import types, Dispatcher, Bot
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


WEBHOOK_PATH = f"/bot/{TOKEN}"
WEBHOOK_URL = "https://c203-62-84-119-83.ngrok.io" + WEBHOOK_PATH

app.include_router(events.router)
app.include_router(notifications.router)


@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)

@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)