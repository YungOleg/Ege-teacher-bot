import random 
from typing import List, Tuple

#? path: ../tasks_db/ru_b4_task.txt 

async def _get_random_pair() -> List[str]:
    with open("C:\\Users\\bilk5\\Desktop\\Ege-teacher-bot\\src\\db\\tasks_db\\static\\ru_b4_task.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        separated_random_line = random_line.split("-")
        right = separated_random_line[0]
        wrong = separated_random_line[1]
        return [right, wrong]


async def _shuffle_pair(pair: List[str]) -> Tuple[List[str], int]:
    answer = 0
    if random.random() < 0.5:
        pair[0], pair[1] = pair[1], pair[0]
        answer = 1
    return (pair, answer)


async def get_b4_quiz() -> Tuple[List[str], int]:
    pair: List[str] = await _get_random_pair()
    task, answer = await _shuffle_pair(pair)
    return (task, answer)