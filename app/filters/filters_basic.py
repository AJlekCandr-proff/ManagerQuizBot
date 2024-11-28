from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter

from ..configuration.settings import settings, views


class AdminFilter(Filter):
    async def __call__(self, event: Message | CallbackQuery) -> Message | None:
        if event.from_user.id == settings.telegram_id_admin:
            return event

        else:
            await event.answer(text=views.get('error_admission'))


class CheckMessage(Filter):
    async def __call__(self, message: Message) -> Message | None:
        if message.text:
            return Message

        else:
            await message.answer(text=views.get('error_text'))
