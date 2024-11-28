from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from app.filters.filters_basic import AdminFilter
from app.configuration.settings import views


router = Router(name=__name__)


@router.message(Command('settings'), AdminFilter())
async def handler_settings(message: Message) -> None:
    """
    Асинхронный обработчик команды /settings.
    Присылает панель администратора для добавления заданий, рассылки и статистики.

    :param message: Объект класса Message.
    """

    await message.answer(text=views.get('panel_settings_view'))
