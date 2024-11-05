from functools import lru_cache

from guide_command import GuideCommand
from settings import Settings


lru_cache(maxsize=None)
def parse_command(message: str) -> None | GuideCommand:
    for command in Settings.COMMANDS:
        if command.command in message:
            return command
