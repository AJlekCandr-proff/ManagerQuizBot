from pydantic import BaseModel, NonNegativeInt, PositiveInt


class PupilProfile(BaseModel):
    telegram_id: PositiveInt
    name: str
    surname: str
    category: str
    points: NonNegativeInt = 0
