from aiogram import Router
from aiogram.types import Message, CallbackQuery

from app.filters.filters_basic import AdminFilter
from app.filters.filters_admin import AdditionFilter


router = Router(name=__name__)


@router.message(AdditionFilter(), AdminFilter())
async def handler_addition_task(callback: CallbackQuery) -> None:
    await callback.message.edit_text(text='🏫 Выбери категорию:')

