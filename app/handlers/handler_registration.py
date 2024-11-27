from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ..configuration.settings import views
from ..filters.filters_registation import RegistrationFilter, EnterName
from ..utils.states_form import States


router = Router(name=__name__)


@router.message(RegistrationFilter())
async def handler_registration(message: Message, state: FSMContext) -> None:
    await message.answer(text=f"{message.from_user.first_name}, {views.get('registration_view')}")

    await message.answer(text=views.get('set_name'))

    await state.set_state(States.get_name)


@router.message(States.get_name, EnterName())
async def handler_get_name(message: Message) -> None:
    await message.answer(text=views.get('choice_category'))
