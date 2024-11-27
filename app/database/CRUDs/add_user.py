from sqlalchemy import insert

from pydantic import ValidationError

from app.configuration.settings import async_session, logger_quiz
from ..models.user import Profiles
from app.validation.user_validation import PupilProfile


async def add_user(values: PupilProfile) -> None:
    """
    Асинхронная функция добавления пользователя в базу данных.

    :param values: Объект класса NewUser.
    """

    try:
        async with async_session() as session:
            query = insert(Profiles).values(values.model_dump())

            await session.execute(query)

            await session.commit()

            return logger_quiz.info(f'Профиль пользователя {values.telegram_id} добавлен в базу данных!')

    except (ValueError, ValidationError):
        return logger_quiz.error('Ошибка в валидации данных при добавлении пользователя в базу данных!')
