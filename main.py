import asyncio
import logging
import sqlite3

from aiogram import Dispatcher, Bot, F, types
from config import BOT_TOKEN
from handlers import router3
from aiogram.types import Message, CallbackQuery
from app import database as db
from aiogram.filters import CommandStart, Command
from app.keyboards import start_keyboard


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



async def on_startup():
    await db.db_start()
    print("Bot started successfully")


async def main():
    dp.include_router(router3)
    await dp.start_polling(bot, on_startup=on_startup)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
