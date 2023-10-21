from user_model import User
from ..db_config import database
import uuid


class TaskRepo():
    
    @staticmethod
    async def retrieve():
        _user = []
        collection = database.get_collection("users").find()
        async for task in collection:
            _user.append(task)
        return _user
    
    @staticmethod
    async def insert(user: User):
        # TODO: Сделать добавление пользователя + проверку на существование
        id = str(uuid.uuid4())
        _user = {
            "_id": id,
            
        }
        await database.get_collection("users").insert_one(_user)
    
    @staticmethod
    async def update(id: str, user: User):
        # TODO: нужно прибавлять количество решенных/нерешенных задач
        _user = await database.get_collection("users").find_one({"_id":id})
        _user["task_id"] = user.task_id
        await database.get_collection("users").update_one({"_id": id}, {"$set": _user})
        ...
    
    @staticmethod
    async def retrieve_id(id: str):
        return await database.get_collection("users").find_one({"_id":id})
    
    @staticmethod
    async def delete(id: str):
        return await database.get_collection("users").delete_one({"_id":id})