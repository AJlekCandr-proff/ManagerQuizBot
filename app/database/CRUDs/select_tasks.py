from sqlalchemy import select

from ..models.tasks import Tasks
from app.configuration.settings import async_session, logger_quiz


async def select_tasks(category: str) -> list[tuple[str, int]]:
    """
    Асинхронная функция для извлечения всех заданий определенной категории (школы).

    :return: Список всех заданий для определенной возрастной категории (школы).
    """

    try:
        async with async_session() as session:
            query = select(Tasks).where(Tasks.category == category)

            tasks = await session.execute(query)

            return tasks.scalars().all()

    except Exception as error:
        logger_quiz.error(f'При извлечении заданий произошла ошибка: {error}')
