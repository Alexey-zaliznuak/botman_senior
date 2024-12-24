import datetime
from aiogram import Bot
from aiogram.types import Message, ChatPermissions


async def mute(bot: Bot, message: Message, target_user_id, until_date):
    await bot.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=target_user_id,
        permissions=ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False
        ),
        until_date=str(until_date)
    )

async def mute_forever(bot, message: Message, target_user_id):
    return await mute(bot, message, target_user_id, datetime.now() + datetime.timedelta(days=3650))
