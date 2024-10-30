import asyncio
from aiogram import Bot, Dispatcher, methods
from aiogram.types import Message, BotCommand

from settings import Settings
from utils import get_command


bot = Bot(token = Settings.BOT_TOKEN)
dp = Dispatcher()

BOT_USERNAME = "@botman_senior_bot"

@dp.message()
async def process_message(message: Message):
    command = get_command(message.text)

    if not command:
        return

    reply_target_message = message
    super_reply = False

    if message.reply_to_message:
        super_reply = True
        reply_target_message = message.reply_to_message

    await reply_target_message.reply(str(command))

    if super_reply and message.text.strip() == command.command or command.command + BOT_USERNAME:
        await message.delete()

# not work....................
async def setup_bot_commands():
    pass
    # commands = [c.as_telegram_command() for c in Settings.COMMANDS]
    # await bot.set_my_commands(commands)

if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot, skip_updates=True, on_startup=setup_bot_commands))
