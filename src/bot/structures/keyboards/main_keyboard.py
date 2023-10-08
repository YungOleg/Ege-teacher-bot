from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

math_button = KeyboardButton(text="Математика")
ru_button = KeyboardButton(text="Русский язык")
#? inf_button = KeyboardButton(text="Информатика")

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [ru_button, math_button]
    ],
    resize_keyboard=True
    )