from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup


def menu_tasks(list_tasks: list[tuple[str, int]]) -> InlineKeyboardMarkup:
    """
    Функция создания inline-клавиатуры с доступными заданиями.

    :param list_tasks: Список заданий и их ID.

    :return: Объект класса InlineKeyboardMarkup.
    """

    inline_builder = InlineKeyboardBuilder()

    for task in list_tasks:
        inline_builder.row(InlineKeyboardButton(text=task[0], callback_data=f'{task[1]}'))

    return inline_builder.as_markup()
