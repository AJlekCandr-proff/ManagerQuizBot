from aiogram.fsm.state import State, StatesGroup


class States(StatesGroup):
    get_name = State()
    get_category = State()


class StatesAdmin(StatesGroup):
    choice_category = State()
    choice_title = State()
    enter_question = State()
    choice_points = State()
