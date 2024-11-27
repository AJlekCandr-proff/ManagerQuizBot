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
