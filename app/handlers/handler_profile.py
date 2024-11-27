from aiogram import Router
from aiogram.types import Message

from ..middlewares.registered_middleware import UserRegisteredMiddleware
from ..filters.filters_profile import ProfileFilter


router = Router(name=__name__)

router.message.middleware(UserRegisteredMiddleware())


@router.message(ProfileFilter())
async def handler_profile(message: Message) -> None:
    """
    Асинхронный обработчик нажатия кнопки "👤 Профиль".
    Присылает пользователю его профиль и активность.

    :param message: Объект класса Message.
    """

    await message.answer(
        text=f""" 
{message.from_user.first_name}, вот твой профиль 🧩\n\n
        """
    )
