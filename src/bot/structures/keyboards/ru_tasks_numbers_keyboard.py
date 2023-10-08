"""Клавиатура с номерами заданий"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_1 = InlineKeyboardButton(
    text="1",
    callback_data="1"
)
button_2 = InlineKeyboardButton(
    text="2",
    callback_data="2"
)
button_3 = InlineKeyboardButton(
    text="3",
    callback_data="3"
)
button_4 = InlineKeyboardButton(
    text="4",
    callback_data="4"
)
button_5 = InlineKeyboardButton(
    text="5",
    callback_data="5"
)
button_6 = InlineKeyboardButton(
    text="6",
    callback_data="6"
)
button_7 = InlineKeyboardButton(
    text="7",
    callback_data="7"
)
button_8 = InlineKeyboardButton(
    text="8",
    callback_data="8"
)
button_9 = InlineKeyboardButton(
    text="9",
    callback_data="9"
)
button_10 = InlineKeyboardButton(
    text="10",
    callback_data="10"
)
button_11 = InlineKeyboardButton(
    text="11",
    callback_data="11"
)
button_12 = InlineKeyboardButton(
    text="12",
    callback_data="12"
)
button_13 = InlineKeyboardButton(
    text="13",
    callback_data="13"
)
button_14 = InlineKeyboardButton(
    text="14",
    callback_data="14"
)
button_15 = InlineKeyboardButton(
    text="15",
    callback_data="15"
)
button_16 = InlineKeyboardButton(
    text="16",
    callback_data="16"
)
button_17 = InlineKeyboardButton(
    text="17",
    callback_data="17"
)
button_18 = InlineKeyboardButton(
    text="18",
    callback_data="18"
)
button_19 = InlineKeyboardButton(
    text="19",
    callback_data="19"
)
button_20 = InlineKeyboardButton(
    text="20",
    callback_data="20"
)
button_21 = InlineKeyboardButton(
    text="21",
    callback_data="21"
)
button_22 = InlineKeyboardButton(
    text="22",
    callback_data="22"
)
button_23 = InlineKeyboardButton(
    text="23",
    callback_data="23"
)
button_24 = InlineKeyboardButton(
    text="24",
    callback_data="24"
)
button_25 = InlineKeyboardButton(
    text="25",
    callback_data="25"
)
button_26 = InlineKeyboardButton(
    text="26",
    callback_data="26"
)
button_27 = InlineKeyboardButton(
    text="27",
    callback_data="27"
)
next_button_10to18 = InlineKeyboardButton(
    text=">>",
    callback_data="next_10to18"
)
back_button_10to18 = InlineKeyboardButton(
    text="<<",
    callback_data="back_10to18"
)
button_1to9 = InlineKeyboardButton(
    text="<<",
    callback_data="1to9"
)
button_19to27 = InlineKeyboardButton(
    text=">>",
    callback_data="19to27"
)

KEYBOARD_1TO9 = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_1, button_2, button_3],
        [button_4, button_5, button_6],
        [button_7, button_8, button_9],
        [next_button_10to18]
    ]
)
KEYBOARD_10TO18 = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_10, button_11, button_12],
        [button_13, button_14, button_15],
        [button_16, button_17, button_18],
        [button_1to9, button_19to27]
    ]
)
KEYBOARD_19TO27 = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_19, button_20, button_21],
        [button_22, button_23, button_24],
        [button_25, button_26, button_27],
        [back_button_10to18]
    ]
)