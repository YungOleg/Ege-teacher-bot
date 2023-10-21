from task_model import Task
from ..db_config import database
import uuid


class TaskRepo():
    
    @staticmethod
    async def retrieve():
        _tasks = []
        collection = database.get_collection("tasks").find()
        async for task in collection:
            _tasks.append(task)
        return _tasks
    
    @staticmethod
    async def insert(task: Task):
        id = str(uuid.uuid4())
        _task = {
            "_id": id,
            "task_id":task.task_id,
            "task_type":task.task_type,
            "task_number":task.task_number,
            "task_question":task.task_question,
            "task":task.task,
            "task_hint":task.task_hint,
            "task_answer":task.task_answer,
            "task_from":task.task_from
        }
        await database.get_collection("tasks").insert_one(_task)
    
    @staticmethod
    async def update(id: str, task: Task):
        _task = await database.get_collection("tasks").find_one({"_id":id})
        _task["task_id"] = task.task_id
        await database.get_collection("tasks").update_one({"_id": id}, {"$set": _task})
        ...
    
    @staticmethod
    async def retrieve_id(id: str):
        return await database.get_collection("tasks").find_one({"_id":id})
    
    @staticmethod
    async def delete(id: str):
        return await database.get_collection("tasks").delete_one({"_id":id})