import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardBuilder, InlineKeyboardMarkup
import sqlite3

TOKEN = ''
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())