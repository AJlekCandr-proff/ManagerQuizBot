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
