#123
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6958363140:AAESBjrvMJLQcJ7ZWtmXOkU7PeXLtOVP0jQ");
dp = Dispatcher()

@dp.message(F)
async def cmd_mih(message: types.Message):
    await message.reply("Денисов")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
