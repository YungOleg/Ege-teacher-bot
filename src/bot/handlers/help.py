from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

help_router = Router(name='help')


@help_router.message(Command(commands='help'))
async def help_handler(message: Message):
    HELP_MESSAGE = "помощь"
    return await message.answer(HELP_MESSAGE)