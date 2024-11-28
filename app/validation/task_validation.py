from pydantic import BaseModel, PositiveInt


class Task(BaseModel):
    title: str
    description: str
    correct_answer: str
    gifs_points: PositiveInt
