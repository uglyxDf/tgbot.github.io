import asyncio
import random
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup

# Твой токен от BotFather
TOKEN = "8851204263:AAHyamueL0OZmhAVORN1uFa0ro-vQMLMDhs"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Эмулируем базу данных баланса (в словаре)
user_balances = {}

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Ссылка на твой сайт на GitHub Pages
    web_app = WebAppInfo(url="https://uglyxdf.github.io/tgbot.github.io/")
    
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть Казино 🎰", web_app=web_app)]
    ])
    
    await message.answer("Добро пожаловать в наше Telegram Казино!", reply_markup=markup)

@dp.message(F.web_app_data)
async def handle_web_app_data(message: types.Message):
    user_id = message.from_user.id
    
    # Инициализация баланса при первом запуске
    if user_id not in user_balances:
        user_balances[user_id] = 100
    
    # Логика игры
    if user_balances[user_id] >= 10:
        user_balances[user_id] -= 10
        
        symbols = ['🍒', '🍋', '💎', '🔔', '⭐️']
        result = [random.choice(symbols) for _ in range(3)]
        
        # Проверка на победу: все три символа одинаковые
        if result[0] == result[1] == result[2]:
            user_balances[user_id] += 50
            win_msg = "🎉 ДЖЕКПОТ! Вы выиграли 50 монет!"
        else:
            win_msg = "😔 Попробуйте еще раз!"
            
        await message.answer(f"Результат: {' '.join(result)}\n{win_msg}\nВаш баланс: {user_balances[user_id]}")
    else:
        await message.answer("Недостаточно средств на балансе!")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())