from typing import List

import dotenv
from pydantic_settings import BaseSettings

from commands import BaseCommand, GuideCommand, SimpleCommand
from normalize import bulk_normalize, normalize_string
from normalize.settings import NORMALIZE_KEYWORD, STOP_KEYWORDS

dotenv.load_dotenv(override=True)


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMINS: list = [1087968824]

    SUPPORT_CHAT_ID: str = "-1002383872514"
    BOT_MAN_CHAT_ID: str = "-1001972329620"

    STOP_KEYWORDS: List[str] = bulk_normalize(STOP_KEYWORDS)
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
            "Контакты техподдержки для сложных запросов. @BotManSupport_bot"),
    ] + sorted([
        # Agents
        GuideCommand("agents", "Агенты", "https://help.botman.pro/article/15881"),

        # Random choise
        GuideCommand("random", "Случайный выбор", "https://help.botman.pro/article/15435"),

        # Actions
        GuideCommand("global_vars", "Действия: Глобальные переменные", "https://help.botman.pro/article/21105"),
        GuideCommand("accept_answer", "Действия: Принять / отклонить ответ пользователя", "https://help.botman.pro/article/18604"),
        GuideCommand("request", "Действия: Внешний запрос", "https://help.botman.pro/article/16068"),
        GuideCommand("vars", "Действия: Переменные", "https://help.botman.pro/article/15494"),
        GuideCommand("start_bot_script", "Действия: Запуск сценария бота", "https://help.botman.pro/article/15459"),
        GuideCommand("admin", "Действия: Отправка данных администратору", "https://help.botman.pro/article/15458"),
        GuideCommand("email", "Действия: Отправка email письма", "https://help.botman.pro/article/15143"),
        GuideCommand("pin", "Действия: Закрепить сообщение", "https://help.botman.pro/article/15140"),
        GuideCommand("approve_application", "Действия: Одобрить заявку в частный канал", "https://help.botman.pro/article/14487"),

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

        # Marks
        GuideCommand("marks", "Метки: создание и настройка", "https://help.botman.pro/article/17094"),

        # Conditions
        GuideCommand("check_marks", "Настройка условий: Проверка наличия метки", "https://help.botman.pro/article/18446"),
        GuideCommand("check_tg_subscription", "Настройка условий: Проверка подписки на канал Telegram", "https://help.botman.pro/article/13981"),
        GuideCommand("check_vk_subscription", "Настройка условий: Проверка подписки на группу VK", "https://help.botman.pro/article/12936"),

        # Events
        GuideCommand("marks_reaction", "Настройка событий: Реагирование на добавление\удаление метки", "https://help.botman.pro/article/16452"),
        GuideCommand("join_private_channel", "Настройка событий: Запуск бота при вступлении в частный канал", "https://help.botman.pro/article/15437"),
        GuideCommand("ref_url", "Настройка событий: Запуск бота по реф. ссылке", "https://help.botman.pro/article/15436"),

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
        GuideCommand("edit_bot", "Настройка бота: Редактирование информации о боте", "https://help.botman.pro/article/15679"),
        GuideCommand("step_params", "Настройка бота: Доп. параметры шага", "https://help.botman.pro/article/20507"),
        GuideCommand("side_menu", "Настройка бота: Боковое меню", "https://help.botman.pro/article/20473"),
        GuideCommand("menu", "Настройка бота: Меню", "https://help.botman.pro/article/15770"),
        GuideCommand("share_phone", "Настройка бота: Поделиться телефоном", "https://help.botman.pro/article/15580"),
        GuideCommand("share_script", "Настройка бота: Поделиться сценарием", "https://help.botman.pro/article/18526"),
        GuideCommand("question", "Настройка бота: Настройка блока вопрос", "https://help.botman.pro/article/14136"),
        GuideCommand("triggers", "Настройка бота: Настройка триггеров запуска бота", "https://help.botman.pro/article/12916"),
        GuideCommand("delay", "Настройка бота: Настройка задержки между сообщениями", "https://help.botman.pro/article/12920"),
        GuideCommand("buttons", "Настройка бота: Настройка кнопок в сообщениях", "https://help.botman.pro/article/12921"),
        GuideCommand("video", "Настройка бота: Настройка отправки видео и видео кружков", "https://help.botman.pro/article/12922"),

        # Interesting solvings
        GuideCommand("send_step", "Интересное: Отправка шага группе подписчиков", "https://help.botman.pro/article/21158"),

        # Connections
        GuideCommand("tg", "Подключение: Telegram", "https://help.botman.pro/article/12623"),
        GuideCommand("vk", "Подключение: VK", "https://help.botman.pro/article/12914"),

    ], key = lambda c: c.description)

    class Config:
        env_file = ".env"

Settings = Settings()



assert len(Settings.COMMANDS) == len(set([c.command for c in Settings.COMMANDS]))  # commands unique const

for el in Settings.STOP_KEYWORDS:
    if Settings.STOP_KEYWORDS.count(el) != 1:
        print(el, Settings.STOP_KEYWORDS.count(el))

assert len(Settings.STOP_KEYWORDS) == len(set(Settings.STOP_KEYWORDS))
assert len(NORMALIZE_KEYWORD) == len(set(NORMALIZE_KEYWORD))


# for c in Settings.COMMANDS:
#     try:
#         print(c.command + " - " + c.description + " - " + c.doc_url)
#     except:
#         print(c.command + " - " + c.description + " - " + c.answer)

#     print()
