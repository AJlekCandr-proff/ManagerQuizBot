from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.keyboards.keyboards import menu_main
from app.configuration.settings import views


router = Router(name=__name__)


@router.message(CommandStart())
async def handler_start(message: Message) -> None:
    """
    Асинхронный обработчик нажатия пользователем команды /start.
    Присылает приветственное сообщение вместе с главным меню.

    :param message: Объект класса Message.
    """

    await message.answer(text=views.get('start_view'), reply_markup=menu_main())
