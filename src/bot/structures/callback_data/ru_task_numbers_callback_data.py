import enum
from aiogram.filters.callback_data import CallbackData


class RuTaskNumberCDAction(enum.IntEnum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    eleven = 11
    twelve = 12
    thirteen = 13
    fourteen = 14
    fifteen = 15
    sixteen = 16
    seventeen = 17
    eighteen = 18
    nineteen = 19
    twenty = 20
    twentyone = 21
    twentytwo = 22
    twentythree = 23
    twentyfour = 24
    twentyfive = 25
    twentysix = 26
    twentyseven = 27

class RuTaskNumberCD(CallbackData, prefix="ru"):
    action: RuTaskNumberCDAction