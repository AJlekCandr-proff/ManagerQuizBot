from aiogram.filters import Filter
from aiogram.types import Message


class RegistrationFilter(Filter):
    async def __call__(self, message: Message) -> Message | None:
        if message.text == '📝 Регистрация':
            return message
