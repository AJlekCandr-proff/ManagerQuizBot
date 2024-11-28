from pydantic import ValidationError
from sqlalchemy import insert

from ..models.tasks import Tasks
from app.validation.task_validation import Task
from app.configuration.settings import async_session, logger_quiz


async def add_tasks(values: Task) -> None:
    """
    Асинхронная функция добавления нового задания в базу данных.

    :param values: Объект класса Task.
    """

    try:
        async with async_session() as session:
            query = insert(Tasks).values(values)

            await session.execute(query)

            await session.commit()

            return logger_quiz.info(f'Новое задание "{values.title}" было успешно добавлено в базу данных!')

    except (ValueError, ValidationError):
        return logger_quiz.error('Ошибка в валидации данных при добавлении нового задания в базу данных!')
