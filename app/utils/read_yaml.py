from yaml import safe_load


def read_views() -> dict[str, str]:
    """
    Функция чтения .yaml-файла с представлениями.

    :return: Словарь представлениями.
    """

    data = {}

    with open('./texts/views.yaml', 'r', encoding='utf-8') as file:
        data.update(safe_load(file))

    return data
