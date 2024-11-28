from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup


def inline_menu_tasks(list_tasks: list[tuple[str, int]]) -> InlineKeyboardMarkup:
    """
    Функция создания inline-клавиатуры с доступными заданиями.

    :param list_tasks: Список заданий и их ID.

    :return: Объект класса InlineKeyboardMarkup.
    """

    inline_builder = InlineKeyboardBuilder()

    for task in list_tasks:
        inline_builder.add(InlineKeyboardButton(text=task[0], callback_data=f'{task[1]}'))

    return inline_builder.adjust(1).as_markup()


def inline_menu_settings() -> InlineKeyboardMarkup:
    """
    Функция создания inline-клавиатуры для панели настроек всей программы.

    :return: Объект класса InlineKeyboardMarkup.
    """

    inline_builder = InlineKeyboardBuilder()

    inline_builder.add(
        InlineKeyboardButton(text='Добавить задание 📚', callback_data='add_task'),
        InlineKeyboardButton(text='Статистика📊', callback_data='quiz_statistic'),
        InlineKeyboardButton(text='Рассылка 🔔', callback_data='create_mailing')
    )

    return inline_builder.adjust(1).as_markup()


def inline_menu_categories() -> InlineKeyboardMarkup:
    """
    Функция создания inline-клавиатуры для выбора категории (школы).

    :return: Объект класса InlineKeyboardMarkup.
    """

    inline_builder = InlineKeyboardBuilder()

    inline_builder.add(
        InlineKeyboardButton(text='Младшая школа (1-4 классы) 🎒', callback_data='Младшая школа (1-4 классы) 🎒'),
        InlineKeyboardButton(text='Средняя школа (5-9 классы) 🏫', callback_data='Средняя школа (5-9 классы) 🏫'),
        InlineKeyboardButton(text='Старшая школа (10-11 классы) 🎓', callback_data='Старшая школа (10-11 классы) 🎓'),
        InlineKeyboardButton(text='Отмена ❌', callback_data='addition_cancel')
    )

    return inline_builder.adjust(1).as_markup()


def inline_menu_points(points: int = 5) -> InlineKeyboardMarkup:
    """
    Функция создания inline-клавиатуры для выбора баллов.

    :return: Объект класса InlineKeyboardMarkup.
    """

    inline_keyboard_builder = InlineKeyboardBuilder()

    inline_keyboard_builder.row(
        InlineKeyboardButton(text='+', callback_data=f'points:{points+1}'),
        InlineKeyboardButton(text=f'{points}', callback_data=f'result:{points}'),
        InlineKeyboardButton(text='-', callback_data=f'points:{points-1}')
    )

    return inline_keyboard_builder.as_markup()


def menu_cancel() -> InlineKeyboardMarkup:
    """
    Функция создания inline-клавиатуры для отмены процесса.

    :return: Объект класса InlineKeyboardMarkup.
    """

    inline_keyboard_builder = InlineKeyboardBuilder()

    inline_keyboard_builder.add(InlineKeyboardButton(text='Отмена ❌', callback_data='addition_cancel'))

    return inline_keyboard_builder.as_markup()
