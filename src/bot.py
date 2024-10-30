import asyncio
from aiogram import Bot, Dispatcher, methods
from aiogram.types import Message, BotCommand

from settings import Settings
from utils import get_command


bot = Bot(token=Settings.BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def process_message(message: Message):
    command = get_command(message.text)

    if not command:
        return

    reply_target_message = message

    if message.reply_to_message:
        reply_target_message = message.reply_to_message

    await reply_target_message.reply(str(command))

    if message.text.strip() == command.command:
        await message.delete()

# not work....................
async def setup_bot_commands():
    commands = [c.as_telegram_command() for c in Settings.COMMANDS]
    await bot.set_my_commands(commands)

if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot, skip_updates=True, on_startup=setup_bot_commands))
