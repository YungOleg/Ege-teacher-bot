import motor.motor_asyncio
from dotenv import load_dotenv

DATABASE_URL = load_dotenv("DATABASE_URL")

client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)

database = client.ege
# TODO: придется использовать еще одну базу данных, отдельно для пользователей