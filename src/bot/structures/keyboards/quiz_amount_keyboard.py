from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

five_button = InlineKeyboardButton(
    text="5",
    callback_data="quiz_5_tasks"
)

ten_button = InlineKeyboardButton(
    text="10",
    callback_data="quiz_10_tasks"
)

fifteen_button = InlineKeyboardButton(
    text="15",
    callback_data="quiz_15_tasks"
)

QUIZ_AMOUNT_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [five_button, ten_button, fifteen_button]
    ]
)