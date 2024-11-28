from re import fullmatch

from aiogram.filters import Filter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ..utils.states_form import States


class RegistrationFilter(Filter):
    async def __call__(self, message: Message) -> Message | None:
        if message.text == '📝 Регистрация':
            return message


class EnterName(Filter):
    async def __call__(self, message: Message, state: FSMContext) -> Message | None:
        if fullmatch(r'^[А-Яа-я]+\s+[А-Яа-я]+$', message.text):
            return message

        else:
            await state.set_state(States.get_name)


class ChoiceCategory(Filter):
    async def __call__(self, message: Message, state: FSMContext) -> Message | None:
        if message.text in [
            'Младшая школа (1-4 классы) 🎒',
            'Средняя школа (5-9 классы) 🏫',
            'Старшая школа (10-11 классы) 🎓'
        ]:
            return message

        else:
            await state.set_state(States.get_category)
