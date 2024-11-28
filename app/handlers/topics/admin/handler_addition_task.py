from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.keyboards.inline_keyboards import inline_menu_categories, menu_cancel, inline_menu_points
from app.filters.filters_basic import AdminFilter
from app.filters.filters_admin import AdditionFilter
from app.configuration.settings import views
from app.utils.states_form import StatesAdmin
from app.callbacks.menu_callbacks import MenuPoints, ChoicePoints


router = Router(name=__name__)


@router.callback_query(AdditionFilter(), AdminFilter())
async def handler_addition_task(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Асинхронный обработчик нажатия кнопки "Добавить задание 📚".
    Присылается меню категорий.

    :param callback: Объект класса CallbackQuery.
    :param state: Объект класса FSMContext.
    """

    await callback.message.edit_text(text=views.get('settings_get_category_view'), reply_markup=inline_menu_categories())

    await state.set_state(StatesAdmin.choice_category)


@router.callback_query(StatesAdmin.choice_category)
async def handler_choice_title(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Асинхронный обработчик выбора возрастной категории.
    Запрашивает название нового задания.

    :param callback: Объект класса CallbackQuery.
    :param state: Объект класса FSMContext.
    """

    await callback.message.edit_text(text=views.get('settings_get_title_view'), reply_markup=menu_cancel())

    await state.set_state(StatesAdmin.choice_title)


@router.message(StatesAdmin.choice_title)
async def handler_get_title(message: Message, state: FSMContext) -> None:
    """
    Асинхронный обработчик ввода названия нового задания.

    :param message: Объект класса Message.
    :param state: Объект класса FSMContext.
    """

    await message.answer(text=views.get('settings_enter_description_view'), reply_markup=menu_cancel())

    await state.set_state(StatesAdmin.enter_question)


@router.message(StatesAdmin.enter_question)
async def handler_enter_question(message: Message, state: FSMContext) -> None:
    """
    Асинхронный обработчик ввода описания (вопроса) задания.
    Запрашивает количество баллов за правильный ответ.

    :param message: Объект класса Message.
    :param state: Объект класса FSMContext.
    """

    await message.answer(text=views.get('settings_choice_points_view'), reply_markup=inline_menu_points())

    await state.set_state(StatesAdmin.choice_points)


@router.callback_query(StatesAdmin.choice_points, MenuPoints.filter())
async def handler_change_point(callback: CallbackQuery, state: FSMContext, callback_data: MenuPoints) -> None:
    """
    Асинхронный обработчик изменения баллов за правильный ответ на вопрос/задание.

    :param callback: Объект класса CallbackQuery.
    :param state: Объект класса FSMContext.
    :param callback_data: Объект класса MenuPoints.
    """

    await callback.message.edit_text(text=views.get('settings_choice_points_view'), reply_markup=inline_menu_points(callback_data.points))

    await state.set_state(StatesAdmin.choice_points)


@router.callback_query(StatesAdmin.choice_points, ChoicePoints.filter())
async def handler_choice_point(callback: CallbackQuery, state: FSMContext, callback_data: ChoicePoints) -> None:
    """
    Асинхронный обработчик выбора баллов за правильный ответ на вопрос/задание.

    :param callback: Объект класса CallbackQuery.
    :param state: Объект класса FSMContext.
    :param callback_data: Объект класса ChoicePoints.
    """

    await callback.message.answer(text=views.get(''))

    await state.set_state()
