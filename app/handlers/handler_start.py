from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from ..keyboards.keyboards import main_menu


router = Router(name=__name__)


@router.message(CommandStart())
async def handler_start(message: Message) -> None:
    """
    Асинхронный обработчик нажатия пользователем команды /start.
    Присылает приветственное сообщение вместе с главным меню.

    :param message: Объект класса Message.
    """

    await message.answer(text='Привет! Добро пожаловать в викторину.', reply_markup=main_menu())
