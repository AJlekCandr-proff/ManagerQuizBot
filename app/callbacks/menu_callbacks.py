from aiogram.filters.callback_data import CallbackData


class MenuPoints(CallbackData, prefix='points'):
    points: int


class ChoicePoints(CallbackData, prefix='result'):
    result: int
