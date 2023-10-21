from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")


class User(BaseModel):
    # TODO: сделать модель пользователя
    id: str = None
    user_name: str
    user_id: str
    