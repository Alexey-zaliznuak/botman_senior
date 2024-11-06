import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message

from deleted_messages_checker import DeletedMessagesTracker
from settings import Settings
from utils import parse_command


BOT_USERNAME = "@botman_senior_bot"

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log", encoding="utf-8", mode="w")
file_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

bot = Bot(token = Settings.BOT_TOKEN)
dp = Dispatcher()


GuideCommandsDeletedMessagesTracker = DeletedMessagesTracker(bot)


@dp.message()
async def process_guide_command(message: Message):
    command = parse_command(message.text)

    if not command:
        return

    text_contains_only_command = message.text.strip() in [command.command, command.command + BOT_USERNAME]
    reply_target_message = message
    super_reply = False

    if message.reply_to_message:
        super_reply = True
        reply_target_message = message.reply_to_message

    await reply_target_message.reply(str(command))

    if super_reply and text_contains_only_command:
        await message.delete()

    await GuideCommandsDeletedMessagesTracker.add_tracking_message(reply_target_message)


async def setup_bot_commands():
    commands = [c.as_telegram_command() for c in Settings.COMMANDS]
    await bot.set_my_commands(commands)

async def main():
    await setup_bot_commands()
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())
