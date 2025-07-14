from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.commands import command_router
from handlers.callbacks import callbacks_router
from aiogram.fsm.storage.memory import MemoryStorage    
from state import fsm_router

from dotenv import load_dotenv
import os

import asyncio

storage = MemoryStorage()

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()   
dp.include_router(callbacks_router)     
dp.include_router(command_router)
dp.include_router(fsm_router)

async def RPGminigame():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML), storage = storage)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(RPGminigame())


    