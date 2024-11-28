from sqlalchemy import select

from ..models.tasks import Tasks
from app.configuration.settings import async_session, logger_quiz


async def select_tasks() -> list[tuple[str, int]]:
    try:
        async with async_session() as session:
            query = select(Tasks)

            tasks = await session.execute(query)

            return tasks.scalars().all()

    except Exception as error:
        print(error)
