import os
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Это была команда старт \nНапиши "Привет" или "Пока" или еще что нибудь', )


@dp.message()
async def echo(message: types.Message):
    text = message.text.lower()

    if text in ['привет', 'привет', 'hello', 'hi']:
        await message.answer('И тебе привет!')
    elif text in ['пока', 'покедова']:
        await message.answer('Пока, надеюсь еще увидимся')
    else:
        await message.answer(text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())