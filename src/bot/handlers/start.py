from aiogram import Router, types
from aiogram.filters import CommandStart

start_router = Router(name='start')


@start_router.message(CommandStart())
async def start_handler(message: types.Message):
    START_MESSAGE = "старт"
    return await message.answer(START_MESSAGE)