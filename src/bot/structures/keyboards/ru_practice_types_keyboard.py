from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from structures.callback_data.ru_callback_data import RuCD, RuCDAction

quiz_mode_button = InlineKeyboardButton(
    text="Квиз❓",
    callback_data=RuCD(action=RuCDAction.QUIZ_MODE).pack()
)
variant_mode_button = InlineKeyboardButton(
    text="Вариант📋",
    callback_data=RuCD(action=RuCDAction.VARIANT_MODE).pack()
)
theme_mode_button = InlineKeyboardButton(
    text="Задания по теме📚",
    callback_data=RuCD(action=RuCDAction.THEME_MODE).pack()
)
theory_mode_button = InlineKeyboardButton(
    text="Теория🧠",
    callback_data=RuCD(action=RuCDAction.THEORY_MODE).pack()
)
modes_info_button = InlineKeyboardButton(
    text="Подробнее о режимах⚙️",
    callback_data="modes_info"
)
close_button = InlineKeyboardButton(
    text="Закрыть❌",
    callback_data="modes_close"
)

RU_PRACTICE_TYPES_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [theory_mode_button, quiz_mode_button],
        [variant_mode_button, theme_mode_button],
        [modes_info_button],
        [close_button]
    ]
)