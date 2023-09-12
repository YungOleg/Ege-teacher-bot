from aiogram import Router, types
from aiogram.filters import Command

help_router = Router(name='help')


@help_router.message(Command(commands='help'))
async def help_handler(message: types.Message):
    HELP_MESSAGE = "помощь"
    return await message.answer(HELP_MESSAGE)