import asyncio
import logging
import emoji

from time import time

from aiogram import F, Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from deleted_messages_checker import DeletedMessagesTracker
from settings import Settings
from utils import parse_time, beauti_time_arg, emojis_count, choose_command
from normalize import normalize_string


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
        # DeletedMessagesTracker.add_tracking_message(message)
        return

    if not message.reply_to_message:
        await message.reply("Выбери сообщение для передачи")
        return

    args = message.text.split()[1:]

    if len(args) == 0:
        await message.reply("Нет параметра")
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
        await mute(bot, message, target_user_id, until_date)
        await message.reply(
            f"Пользователь {message.reply_to_message.from_user.full_name} теперь отдыхает {beauti_time_arg(time_arg)}."
        )

    except Exception as e:
        logger.error("Error when trying to mute: " + str(e))
        await message.reply(f"Что то пошло не так(")


@dp.message(Command("ban"))
async def ban_handler(message: Message):
    if message.from_user.id not in Settings.ADMINS:
        await message.delete()
        return

    args = message.text.split()[1:]

    user_id = args[0]

    try:
        await bot.ban_chat_member(message.chat.id, user_id)
        logger.error("Success bun: " + str(user_id))
        await bot.send_message(Settings.SUPPORT_CHAT_ID, f"Пользователь с id {user_id} заблочен", parse_mode="html")

    except ValueError as e:
        logger.error("Error when trying to mute: " + str(e))
        return

    await message.delete()


@dp.message(
    lambda message: bool(
        message.chat.id != int(Settings.SUPPORT_CHAT_ID)
        and (
            message.forward_date
            or emojis_count(message.text) >= 7
            or (
                message.text
                and any([kw in normalize_string(message.text) for kw in Settings.STOP_KEYWORDS])
            )
        )
    )
)
async def validate_illegal(message: Message):
    logger.info(f"Remove message from {message.from_user.username}, id: {message.from_user.id}, text: {message.text}")

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Бан", callback_data=f"ban_{message.from_user.id}_{message.chat.id}")]
        ]
    )

    await bot.forward_message(Settings.SUPPORT_CHAT_ID, message.chat.id, message.message_id)

    await message.delete()

    await bot.send_message(
        Settings.SUPPORT_CHAT_ID,
        f"Подозрительное сообщение",
        reply_markup=keyboard if message.from_user.username != "GroupAnonymousBot" else None,
        parse_mode="html",
    )


@dp.callback_query(lambda callback_query: "ban_" in callback_query.data)
async def handle_ban_callback(callback_query: CallbackQuery):
    _, user_id, chat_id = callback_query.data.split("_")

    await bot.answer_callback_query(callback_query.id)

    try:
        await bot.ban_chat_member(chat_id, user_id)
        logger.error("Success bun by button callback: " + str(user_id))
        await bot.send_message(Settings.SUPPORT_CHAT_ID, f"Пользователь с id {user_id} заблочен", parse_mode="html")

    except ValueError as e:
        logger.error("Error when trying to mute: " + str(e))
        return


@dp.message(Command("get_chat_id"))
async def get_chat_id(message: Message):
    chat = await bot.get_chat(message.chat.id)
    await message.answer(f"Новый ID чата: {chat.id}")


@dp.message()
async def support_commands_handler(message: Message) -> bool:
    if message.text is None:
        return

    command = choose_command(message.text)

    if not command:
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
