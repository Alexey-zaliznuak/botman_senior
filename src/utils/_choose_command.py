from functools import lru_cache

from aiogram import Bot
from aiogram.types import Message

from commands import GuideCommand
from settings import Settings

lru_cache(maxsize=None)
def choose_command(message_text: str) -> None | GuideCommand:
    for command in Settings.COMMANDS:
        if command.check_message_contains_command(message_text):
            return command
