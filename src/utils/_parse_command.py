from functools import lru_cache

from commands import GuideCommand
from settings import Settings


lru_cache(maxsize=None)
def parse_command(message: str) -> None | GuideCommand:
    for command in Settings.COMMANDS:
        try:
            if command.command in message:
                return command
        except:
            raise RuntimeError("AAAAAAAAAA", command.__dict__)