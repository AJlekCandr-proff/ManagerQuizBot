from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, String, BigInteger

from .base import Base


class Tasks(Base):
    __tablename__ = 'tasks'

    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    gifs_points: Mapped[int] = mapped_column(BigInteger, nullable=False, default=5)
