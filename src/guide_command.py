from aiogram.types import BotCommand


COMMAND_PREFIX = "/"


class GuideCommand:
    BASE_GUIDE_ANSWER_MESSAGE: str = "Конечно, держите наш гайд!"

    def __init__(self, command: str, description: str, doc_url: str, about: str | None = None):
        """
        :param command: Command, example: 'start'
        :param description: Description of command, example: 'restart this bot'
        :param doc_url: Documentation link.
        :param about: Short description.
        """
        self.command = COMMAND_PREFIX + command
        self.description = description
        self.doc_url = doc_url
        self.guide_summary = about

    def __str__(self):
        """
        Bot message when triggers on this command
        """
        return (
            f"{self.BASE_GUIDE_ANSWER_MESSAGE}"
            + "\n"
            + self.doc_url
            + (("\n"*2 + "Если вкратце:" + "\n" + self.guide_summary) if self.guide_summary else "")
        )

    def get_info(self) -> dict:
        return {
            "command": self.command,
            "doc_url": self.doc_url,
            "guide_summary": self.guide_summary
        }

    def as_telegram_command(self) -> BotCommand:
        return BotCommand(command=self.command, description=self.description)
