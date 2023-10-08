from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from structures.keyboards.main_keyboard import MAIN_KEYBOARD

start_router = Router(name='start')


@start_router.message(Command(commands='start'))
async def start_handler(message: Message):
    START_MESSAGE = "Привет!"
    return await message.answer(text=START_MESSAGE, reply_markup=MAIN_KEYBOARD)