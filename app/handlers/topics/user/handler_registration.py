from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.configuration.settings import views
from app.filters.filters_registation import RegistrationFilter, EnterName, ChoiceCategory
from app.filters.filters_basic import CheckMessage
from app.utils.states_form import States
from app.keyboards.keyboards import categories_menu, main_menu
from app.database.CRUDs.add_user import add_user
from app.validation.user_validation import PupilProfile
from app.middlewares.is_not_registered_middleware import UserNotRegisteredMiddleware


router = Router(name=__name__)

router.message.middleware(UserNotRegisteredMiddleware())


@router.message(RegistrationFilter())
async def handler_registration(message: Message, state: FSMContext) -> None:
    """
    Асинхронный обработчик нажатия кнопки "📝 Регистрация".
    Начинает регистрацию пользователя на проекте.

    :param message: Объект класса Message.
    :param state: Объект класса FSMContext.
    """

    await message.answer(text=f"{message.from_user.first_name}, {views.get('registration_view')}")

    await message.answer(text=views.get('set_name'))

    await state.set_state(States.get_name)


@router.message(States.get_name, CheckMessage(), EnterName())
async def handler_get_name(message: Message, state: FSMContext) -> None:
    """
    Асинхронный обработчик ввода имени и фамилии ученика для регистрации.

    :param message: Объект класса Message.
    :param state: Объект класса FSMContext.
    """

    await message.answer(text=views.get('choice_category'), reply_markup=categories_menu())

    await state.update_data(name=message.text)

    await state.set_state(States.get_category)


@router.message(States.get_category, CheckMessage(), ChoiceCategory())
async def handler_choice_category(message: Message, state: FSMContext) -> None:
    """
    Асинхронный обработчик выбора школы (Младшая, средняя и старшая),
    завершение регистрации пользователя в проекте.

    :param message: Объект класса Message.
    :param state: Объект класса FSMContext.
    """

    data = await state.get_data()

    user_name = data.get('name')
    name = user_name.split(' ')[0]
    surname = user_name.split(' ')[1]

    user = PupilProfile(telegram_id=message.from_user.id, name=name, surname=surname, category=message.text)

    await add_user(user)

    await message.answer(text=views.get('finally_registration'), reply_markup=main_menu())

    await state.clear()
