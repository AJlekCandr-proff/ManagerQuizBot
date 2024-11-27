from aiogram import Router
from aiogram.types import Message

from ..configuration.settings import views
from ..filters.filters_registation import RegistrationFilter


router = Router(name=__name__)


@router.message(RegistrationFilter())
async def handler_registration(message: Message) -> None:
    await message.answer(text=f"{message.from_user.first_name}, {views.get('registration_view')}")
