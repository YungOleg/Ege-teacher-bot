import random 
from typing import List, Tuple


async def _get_random_pair() -> List[str]:
    with open("C:\\Users\\bilk5\\Desktop\\Ege-teacher-bot\\src\\db\\tasks_db\\static\\ru_b5_task.txt", "r", encoding="utf-8") as file:
        lines = file.read()
        separated_lines = lines.split("\n\n")
        task = random.choice(separated_lines)
        return task


async def _get_task(pair: str) -> Tuple[str, int, List[str]]:
    separated_pair = pair.split("\n")
    separated_answer = separated_pair[1].split('-')
    task = separated_pair[0].capitalize()
    answer = list(map(lambda x: x.lower().strip(), separated_answer))
    right_index = separated_answer.index([ans for ans in separated_answer if ans.isupper()][0])
    return task, right_index, answer


async def get_b5_quiz() -> Tuple[str, int, List[str]]:
    pair = await _get_random_pair()
    task, right_answer, answers = await _get_task(pair)
    return (task, right_answer, answers)