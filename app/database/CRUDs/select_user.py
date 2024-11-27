from pydantic import ValidationError

from sqlalchemy import select

from ..models.user import Profiles
from app.validation.user_validation import PupilProfile
from app.configuration.settings import async_session, logger_quiz


async def select_user(value: int) -> PupilProfile | None:
    """
    Асинхронная функция для извлечения (поиска) профиля пользователя из базы данных.

    :param value: Telegram ID пользователя.

    :return: Объект класса PupilProfile, либо None.
    """

    try:
        async with async_session() as session:
            query = select(Profiles).where(Profiles.telegram_id == value)

            user = await session.execute(query)
            user = user.scalar()

            return PupilProfile(
                telegram_id=user.telegram_id,
                name=user.name,
                surname=user.surname,
                category=user.category,
                points=user.points
            )

    except (ValueError, ValidationError):
        return logger_quiz.error(f'Ошибка при извлечении профиля пользователя: Такого профиля не существует!')
