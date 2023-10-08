import enum
from aiogram.filters.callback_data import CallbackData


class RuCDAction(enum.IntEnum):
    QUIZ_MODE = 0
    THEME_MODE = 1
    VARIANT_MODE = 2
    THEORY_MODE = 3

class RuCD(CallbackData, prefix="ru"):
    action: RuCDAction