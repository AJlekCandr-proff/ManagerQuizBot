from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, BigInteger

from .base import Base


class Profiles(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    name: Mapped[str] = mapped_column(String(15), nullable=False)
    surname: Mapped[str] = mapped_column(String(15), nullable=False)
    category: Mapped[str] = mapped_column(String(15), nullable=False)
    points: Mapped[int] = mapped_column(BigInteger, nullable=True)
