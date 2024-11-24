import asyncio
import logging
from time import time

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message, ChatPermissions

from deleted_messages_checker import GROUP_ANONYMOUS_BOT, DeletedMessagesTracker
from settings import Settings
from utils import choose_command, parse_time, beauti_time_arg, emojis


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log", encoding="utf-8", mode="w")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


bot = Bot(token = Settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode="Markdown"))
dp = Dispatcher()

DeletedMessagesTracker = DeletedMessagesTracker(bot)


@dp.message(Command("mute"))
async def mute_handler(message: Message):
    if message.from_user.id not in Settings.ADMINS:
        await message.reply(emojis.thinking)
        DeletedMessagesTracker.add_tracking_message(message)

    if not message.reply_to_message:
        await message.reply("Не понимаю, кого мутить(")
        return


    args = message.text.split()[1:]

    if len(args) == 0:
        await message.reply("Нет параметра на сколько мутить")
        return

    time_arg = args[0]

    try:
        mute_duration = parse_time(time_arg)

    except ValueError as e:
        logger.error("Error when trying to mute: " + str(e))
        await message.reply("Не понимаю на сколько времени мутить")
        return

    until_date = int(time()) + mute_duration
    target_user_id = message.reply_to_message.from_user.id

    try:
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=target_user_id,
            permissions=ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False
            ),
            until_date=str(until_date)
        )
        await message.reply(
            f"Пользователь {message.reply_to_message.from_user.full_name} теперь отдыхает {beauti_time_arg(time_arg)}.")

    except Exception as e:
        logger.error("Error when trying to mute: " + str(e))
        await message.reply(f"Что то пошло не так(")


@dp.message()
async def support_commands_handler(message: Message):
    if message.text is None:
        return

    command = choose_command(message.text)

    if not command:
        return

    if message.from_user.id not in Settings.ADMINS:
        await message.delete()
        return

    reply_target_message = message
    super_reply = False

    if message.reply_to_message:
        super_reply = True
        reply_target_message = message.reply_to_message

    await reply_target_message.reply(command.get_answer(bot, message))

    logger.info(f"Command made by {message.from_user.username}, bot answer on message of {reply_target_message.from_user.username}")
    if super_reply and command.check_message_contains_only_command(bot, message):
        await message.delete()
    else:
        # No tracks message which is indirect trigger
        await DeletedMessagesTracker.add_tracking_message(reply_target_message)


async def setup_bot_commands():
    commands = [c.as_telegram_command for c in Settings.COMMANDS]
    await bot.set_my_commands(commands)

async def main():
    await setup_bot_commands()
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())
