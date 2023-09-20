import logging
from aiogram import Bot, Dispatcher, types
import executor as executor
from db import Database

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6547583951:AAG02e7k37PQddhYNG8PlYYlzQ0FmydgIQ4")
dp = Dispatcher(bot)
db = Database('database0')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Dobro pojalovat!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)