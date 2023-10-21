from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")


class Task(BaseModel):
    id: str = None
    task_id: str
    task_type: str
    task_number: str
    task_question: str
    task: str
    task_hint: str
    task_answer: str
    task_from: str