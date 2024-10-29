import asyncio
from aiogram import Bot, Dispatcher, methods
from aiogram.types import Message, BotCommand

from settings import Settings
from utils import get_command


bot = Bot(token=Settings.BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def process_message(message: Message):
    print("Сообщение получено")
    command = get_command(message.text)

    # Проверка, является ли текущее сообщение ответом на другое
    if command:
        print("Найдена команда", command.description)
        target_message = message.reply_to_message or message  # если есть ответ, выбираем его, иначе текущее сообщение
        await target_message.reply(str(command) or "cmd")
    else:
        print("Гайд не выбран")


# not work....................
async def setup_bot_commands():
    commands = [c.as_telegram_command() for c in Settings.COMMANDS]
    await bot.set_my_commands(commands)

if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot, skip_updates=True, on_startup=setup_bot_commands))
