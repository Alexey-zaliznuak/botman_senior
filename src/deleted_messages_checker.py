import asyncio
from dataclasses import dataclass
import logging
from time import time

from aiogram import Bot
from aiogram.types import Message


logger = logging.getLogger()



@dataclass
class TrackingMessage:
    id: int
    chat_id: int

    started_tracking_at: int
    tracking_will_be_stopped_at: int

    author_username: str | None

    text: str


class DeletedMessagesTracker:
    messages: list[TrackingMessage] = []
    bot: Bot

    tracking_delay = 4

    tracking_started = False

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    async def add_tracking_message(self, message: Message, tracking_time: int = 3600):
        await self.start_tracking_if_need()

        self.messages.append(TrackingMessage(
            id=message.message_id,
            chat_id=message.chat.id,

            started_tracking_at=time(),
            tracking_will_be_stopped_at=time() + tracking_time,

            author_username=message.from_user.username,
            text=message.text,
        ))

        logger.info(f"New message tracking from {message.from_user.username}")


    async def tracking(self):
        self.remove_old_messages()

        for message in self.messages:
            await self.process_tracking_message(message)

        await asyncio.sleep(self.tracking_delay)
        asyncio.tasks.create_task(coro=self.tracking())


    async def process_tracking_message(self, message: TrackingMessage):
        if not await self.check_message_exists(message.id, message.chat_id):
            await self.bot.send_message(
                    message.chat_id,
                    f"@{message.author_username}, зачем удаляете свои сообщения?)"
                )
            self.messages.remove(message)

    def remove_old_messages(self):
        messages_count_before_cleaning = len(self.messages)

        logger.debug(f"Кол-во отслеживаемых сообщений до очистки: {messages_count_before_cleaning}")

        self.messages = list(filter(lambda msg: msg.tracking_will_be_stopped_at > time(), self.messages))

        logger.debug(
            "Кол-во отслеживаемых сообщений после очистки: "
            f"{len(self.messages)}, удалено: {len(self.messages) - messages_count_before_cleaning}"
        )


    async def start_tracking_if_need(self):
        if not self.tracking_started:
            self.tracking_started = True
            await asyncio.tasks.create_task(coro=self.tracking())


    async def check_message_exists(self, message_id, chat_id):
        try:
            await self.bot.set_message_reaction(chat_id, message_id, None)
        except Exception as e:
            match str(e):
                case "Telegram server says - Bad Request: REACTION_EMPTY":
                    return True

                case "Telegram server says - Bad Request: MESSAGE_ID_INVALID":
                    print("AAAAAAAAAAAAAAAAAAAAA", chat_id, message_id)
                    return False

                case "Telegram server says - Bad Request:  message to react not found":
                    return False

            raise e
