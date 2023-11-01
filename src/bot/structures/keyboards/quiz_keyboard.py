from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

more_button = InlineKeyboardButton(
    text="Ещё",
    callback_data="more_quiz"
)
quit_button = InlineKeyboardButton(
    text="Выйти",
    callback_data="quit_quiz"
)

QUIZ_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [more_button, quit_button]
    ]
)