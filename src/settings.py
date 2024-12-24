from typing import List

import dotenv
from pydantic_settings import BaseSettings

from commands import BaseCommand, GuideCommand, SimpleCommand

dotenv.load_dotenv(override=True)


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMINS: list = [1087968824]
    STOP_KEYWORDS: List[str] = ["доход от", "без опыта и вложений"]
    COMMANDS: List[BaseCommand] = \
    [
        SimpleCommand(
            "course",
            "Бесплатный курс по созданию автоворонки",
            "Наш бесплатный курс по созданию своей автоворонки [здесь](https://t.me/BotManKurs_bot)"),
        SimpleCommand(
            "service",
            "Заказать бота под ключ",
            "Вы можете заказать разработку бота под-ключ написав [сюда](https://t.me/BotManForCreate_bot)"),
        SimpleCommand(
            "cancel_pro",
            "Отказаться от про тарифа",
            "Вы можете вернуть средства за оплаченный тариф.\n\nДля этого необходимо отправить письмо по форме пункта 7 [оферты](https://botman.pro/files/terms.pdf)."),
    ] + sorted([
        # Agents
        GuideCommand("agents", "Агенты", "https://help.botman.pro/article/15881"),


        # Random choise
        GuideCommand("random", "Случайный выбор", "https://help.botman.pro/article/15435"),


        # Actions
        GuideCommand("global_vars", "Глобальные переменные", "https://help.botman.pro/article/21105"),
        GuideCommand("accept_answer", "Принять / отклонить ответ пользователя", "https://help.botman.pro/article/18604"),
        GuideCommand("request", "Внешний запрос", "https://help.botman.pro/article/16068"),
        GuideCommand("vars", "Переменные", "https://help.botman.pro/article/15494"),
        GuideCommand("start_bot_script", "Запуск сценария бота", "https://help.botman.pro/article/15459"),
        GuideCommand("admin", "Отправка данных администратору", "https://help.botman.pro/article/15458"),
        GuideCommand("email", "Отправка email письма", "https://help.botman.pro/article/15143"),
        GuideCommand("pin", "Закрепить сообщение", "https://help.botman.pro/article/15140"),
        GuideCommand("approve_application", "Одобрить заявку в частный канал", "https://help.botman.pro/article/14487"),


        # Integrations
        GuideCommand("robokassa", "Интеграция с робокассой", "https://help.botman.pro/article/20474"),
        GuideCommand("getcourse_payment", "Интеграция с оплатой GetCourse", "https://help.botman.pro/article/20068"),
        GuideCommand("tinkoff", "Интеграция с Тинькофф эквайринг", "https://help.botman.pro/article/16521"),
        GuideCommand("google", "Интеграция с Гугл таблицами", "https://help.botman.pro/article/15581"),
        GuideCommand("getcourse", "Интеграция с GetCourse", "https://help.botman.pro/article/15531"),
        GuideCommand("amo", "Интеграция с AmoCRM", "https://help.botman.pro/article/15480"),
        GuideCommand("ukassa", "Интеграция с ЮКасса", "https://help.botman.pro/article/14411"),
        GuideCommand("prodamus", "Интеграция с Prodamus", "https://help.botman.pro/article/14378"),
        GuideCommand("umoney", "Интеграция с ЮМани", "https://help.botman.pro/article/14362"),
        # GuideCommand("zvonok", "Интеграция с Zvonok", ""),


        # Marks
        GuideCommand("marks", "Метки: создание и настройка", "https://help.botman.pro/article/17094"),


        # Conditions
        GuideCommand("check_marks", "Условия: Проверка наличия метки", "https://help.botman.pro/article/18446"),
        GuideCommand("check_tg_subscription", "Проверка подписки на канал Telegram", "https://help.botman.pro/article/13981"),
        GuideCommand("check_vk_subscription", "Проверка подписки на группу VK", "https://help.botman.pro/article/12936"),

        # Events
        GuideCommand("marks_reaction", "События: Реагирование на добавление\удаление метки", "https://help.botman.pro/article/16452"),
        GuideCommand("join_private_channel", "События: Запуск бота при вступлении в частный канал", "https://help.botman.pro/article/15437"),
        GuideCommand("ref_url", "Запуск бота по реф. ссылке", "https://help.botman.pro/article/15436"),

        # Tariffs
        GuideCommand(
            "tariffs",
            "Тарифы",
            "https://help.botman.pro/article/18437",
            (
                "Есть бесплатный тариф с ограниченным функционалом, до 1000 подписчиков." + "\n\n"
                "Платные тарифы вы настраиваете сами, они не имеют ограничений по функционалу(кроме рассылок)" + "\n\n"
                "Но ограничены количеством подписчиков, исключение - безлимитный тариф." + "\n\n"
                "Рекомендую перейти на страницу с тарифами и начать настраивать свой про тариф, чтобы узнать конечную стоимость." + "\n\n"
                "Страница с тарифами: https://app.botman.pro/app/tariffs"
            )
        ),

        # Basics
        GuideCommand("edit_bot", "Редактирование информации о боте", "https://help.botman.pro/article/15679"),
        GuideCommand("step_params", "Доп. параметры шага", "https://help.botman.pro/article/20507"),
        GuideCommand("side_menu", "Боковое меню", "https://help.botman.pro/article/20473"),
        GuideCommand("menu", "Меню", "https://help.botman.pro/article/15770"),
        GuideCommand("share_phone", "Поделиться телефоном", "https://help.botman.pro/article/15580"),
        GuideCommand("share_script", "Поделиться сценарием", "https://help.botman.pro/article/18526"),
        GuideCommand("question", "Настройка блока вопрос", "https://help.botman.pro/article/14136"),
        GuideCommand("triggers", "Настройка триггеров запуска бота", "https://help.botman.pro/article/12916"),
        GuideCommand("delay", "Настройка задержки между сообщениями", "https://help.botman.pro/article/12920"),
        GuideCommand("buttons", "Настройка кнопок в сообщениях", "https://help.botman.pro/article/12921"),
        GuideCommand("video", "Настройка отправки видео и видео кружков", "https://help.botman.pro/article/12922"),

        # Interesting solvings
        GuideCommand("send_step", "Отправка шага группе подписчиков", "https://help.botman.pro/article/21158"),

    ], key = lambda c: c.description)

    class Config:
        env_file = ".env"

Settings = Settings()

assert len(Settings.COMMANDS) == len(set([c.command for c in Settings.COMMANDS]))  # commands unique const
# assert len(Settings.COMMANDS) == len(set([c.doc_url for c in Settings.COMMANDS]))  # doc urls unique const

if __name__ == "__main__":
    result = ""
    for command in Settings.COMMANDS:
        result += command.command[1:] + " - " + command.description + "\n"

    print(result)
    print("TOTAL:", len(Settings.COMMANDS))
