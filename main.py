import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup

# FIXME: Нужно вынести токен в .env файл, чтобы не светить его в коде
TOKEN = "8851204263:AAHyamueL0OZmhAVORN1uFa0ro-vQMLMDhs"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Эта кнопка открывает Web App
    web_app = WebAppInfo(url="https://uglyxdf.github.io/uglyxDf.gihub.io/") # Сюда позже вставим ссылку на твой фронтенд
    
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть магазин", web_app=web_app)]
    ])
    
    await message.answer("Привет! Нажми кнопку ниже, чтобы открыть наш магазин:", reply_markup=markup)

from aiogram import F

@dp.message(F.web_app_data)
async def handle_web_app_data(message: types.Message):
    data = message.web_app_data.data
    await message.answer(f"Получен заказ из Mini App: {data}")
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())