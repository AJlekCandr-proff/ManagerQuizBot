from aiogram.filters import Filter
from aiogram.types import Message


class ProfileFilter(Filter):
    async def __call__(self, message: Message) -> Message | None:
        if message.text == '👤 Профиль':
            return message
