from sqlalchemy import insert

from pydantic import ValidationError

from app.configuration.settings import async_session, logger_quiz
from ..models.user import Profiles
from app.validation.user_validation import NewUser


async def add_user(values: NewUser) -> None:
    try:
        async with async_session() as session:
            query = insert(Profiles).values(values.model_dump())

            await session.execute(query)

            await session.commit()
    except (ValueError, ValidationError):
        logger_quiz.error('Ошибка в валидации данных при добавлении пользователя в базу данных!')
