from aiogram import Router
from aiogram.types import Message

from app.middlewares.is_registered_middleware import UserRegisteredMiddleware
from app.filters.filters_profile import ProfileFilter
from app.database.CRUDs.select_user import select_user


router = Router(name=__name__)

router.message.middleware(UserRegisteredMiddleware())


@router.message(ProfileFilter())
async def handler_profile(message: Message) -> None:
    """
    Асинхронный обработчик нажатия кнопки "👤 Профиль".
    Присылает пользователю его профиль и активность.

    :param message: Объект класса Message.
    """

    user = await select_user(message.from_user.id)

    await message.answer(
        text=f""" 
{message.from_user.first_name}, вот твой профиль 🧩\n
🆔 <u>{user.telegram_id}</u>
🎓 {user.name} {user.surname}
📚 <b>Категория:</b> {user.category}
🏅 <b>Баллы:</b> <code>{user.points}</code>\n\n """
    )
