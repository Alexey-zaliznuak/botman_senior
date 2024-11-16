from typing import Any

from aiogram import Bot
from aiogram.types import BotCommand, Message


class BaseCommand:
    COMMAND_PREFIX = "/"
    SHOWNS_IN_COMMANDS_LIST = True
    RETURN_TEXT = True

    def __init__(
        self,
        command: str,
        description: str | None,
        answer: str | None,
    ) -> None:
        self.command = command
        self.description = description
        self.answer = answer

    def check_message_contains_command(self, message_text: str) -> bool:
        return self.command in message_text

    def check_message_contains_only_command(self, bot: Bot, message: Message) -> bool:
        return message.text in [self.COMMAND_PREFIX + self.command, self.COMMAND_PREFIX + self.command + bot._me.username]

    def get_answer(self, bot: Bot, message: Message, context: Any = {}):
        return self.answer

    def before_sending_message(self, bot: Bot, message: Message, context: Any = {}):
        pass

    def after_sending_message(self, bot: Bot, message: Message, context: Any = {}):
        pass

    @property
    def as_telegram_command(self) -> BotCommand:
        return BotCommand(command=self.command, description=self.description)


class SimpleCommand(BaseCommand):
    pass


class GuideCommand(BaseCommand):
    BASE_GUIDE_ANSWER_MESSAGE: str = "Конечно, держите наш гайд!"

    def __init__(self, command: str, description: str, doc_url: str, about: str | None = None):
        """
        :param command: Command, example: 'start'
        :param description: Description of command, example: 'restart this bot'
        :param doc_url: Documentation link.
        :param about: Short description.
        """

        super().__init__(
            command,
            description,
            (
                f"{self.BASE_GUIDE_ANSWER_MESSAGE}"
                + "\n"
                + doc_url
                + (("\n"*2 + about) if about else "")
            )
        )
