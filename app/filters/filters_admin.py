from aiogram.filters import Filter
from aiogram.types import Message, CallbackQuery


class AdditionFilter(Filter):
    async def __call__(self, callback: CallbackQuery) -> CallbackQuery | None:
        if callback.data == 'add_task':
            return callback
