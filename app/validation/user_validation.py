from pydantic import BaseModel, PositiveInt


class NewUser(BaseModel):
    telegram_id: PositiveInt
    name: str
    surname: str
    category: str
    points: PositiveInt
