from aiogram.filters import Filter

from aiogram.types import Message


class TasksFilter(Filter):
    async def __call__(self, message: Message) -> Message | None:
        if message.text == '📖 Мои задания':
            return message
