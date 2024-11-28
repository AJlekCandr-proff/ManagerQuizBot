from aiogram.utils.keyboard import ReplyKeyboardMarkup, ReplyKeyboardBuilder, KeyboardButton


def menu_main() -> ReplyKeyboardMarkup:
    """
    Функция создания клавиатуры для главного меню пользователя.

    :return: Объект класса ReplyKeyboardMarkup.
    """

    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.row(KeyboardButton(text='📖 Мои задания'))
    keyboard_builder.row(KeyboardButton(text='👤 Профиль'), KeyboardButton(text='📝 Регистрация'))

    return keyboard_builder.as_markup(resize_keyboard=True)


def menu_categories() -> ReplyKeyboardMarkup:
    """
    Функция создания клавиатуры для выбора школы (Младшей, средней или старшей) пользователем.

    :return: Объект класса ReplyKeyboardMarkup.
    """

    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.add(
        KeyboardButton(text='Младшая школа (1-4 классы) 🎒'),
        KeyboardButton(text='Средняя школа (5-9 классы) 🏫'),
        KeyboardButton(text='Старшая школа (10-11 классы) 🎓')
    )

    return keyboard_builder.adjust(1).as_markup(resize_keyboard=True)
