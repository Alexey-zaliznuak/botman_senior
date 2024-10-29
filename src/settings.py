from typing import List

from pydantic_settings import BaseSettings

from guide_command import GuideCommand


class Settings(BaseSettings):
    BOT_TOKEN: str
    COMMANDS: List[GuideCommand] = sorted([
        GuideCommand("admin_action", "Отправка данных администратору", "https://help.botman.pro/article/15458"),
        GuideCommand("agents", "Агенты", "https://help.botman.pro/category/3614"),
        GuideCommand("menu", "Меню", "https://help.botman.pro/article/15770"),
        GuideCommand("vars", "Переменные", "https://help.botman.pro/article/15494"),
        GuideCommand("global_vars", "Глобальные переменные", "https://help.botman.pro/article/21105"),
        GuideCommand("tinkoff", "Тинькофф эквайринг", "https://help.botman.pro/article/16521"),
    ], key = lambda c: c.description)

    class Config:
        env_file = ".env"

Settings = Settings()

if __name__ == "__main__":
    result = ""
    for command in Settings.COMMANDS:
        result += command.command[1:] + " - " + command.description + "\n"

    print(result)
