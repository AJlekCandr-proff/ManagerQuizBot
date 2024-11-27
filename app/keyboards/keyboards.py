from aiogram.utils.keyboard import ReplyKeyboardMarkup, ReplyKeyboardBuilder, KeyboardButton


def main_menu() -> ReplyKeyboardMarkup:
    """
    Функция создания клавиатуры для главного меню пользователя.

    :return: Объект класса ReplyKeyboardMarkup.
    """

    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.row(KeyboardButton(text='📖 Мои задания'))
    keyboard_builder.row(KeyboardButton(text='👤 Профиль'), KeyboardButton(text='📝 Регистрация'))

    return keyboard_builder.as_markup(resize_keyboard=True)


def categories_menu() -> ReplyKeyboardMarkup:
    """
    Функция создания клавиатуры для выбора школы (Младшей, средней или старшей) пользователем.

    :return: Объект класса ReplyKeyboardMarkup.
    """

    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.row(KeyboardButton(text='Младшая школа (1-4 классы) 🎒'))
    keyboard_builder.row(KeyboardButton(text='Средняя школа (5-9 классы) 🏫'))
    keyboard_builder.row(KeyboardButton(text='Старшая школа (10-11 классы) 🎓'))

    return keyboard_builder.as_markup(resize_keyboard=True)
