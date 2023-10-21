from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from structures.keyboards.ru_practice_types_keyboard import RU_PRACTICE_TYPES_KEYBOARD
from structures.keyboards.quiz_amount_keyboard import QUIZ_AMOUNT_KEYBOARD
from structures.callback_data.ru_callback_data import RuCD, RuCDAction
from src.db.tasks_db.static.ru_b4 import get_b4_quiz

ru_router = Router(name='ru')

@ru_router.message(F.text=="Русский язык")
async def training_types(message: Message):
    await message.answer(text="Выбери режим тренировки📊", reply_markup=RU_PRACTICE_TYPES_KEYBOARD)

"""
[theory_mode_button],
[quiz_mode_button, ],
[variant_mode_button, theme_mode_button],
[modes_info_button],
[close_button]
"""


@ru_router.callback_query(RuCD.filter(F.action == RuCDAction.THEORY_MODE))
async def theory_mode_ru(call: CallbackQuery):
    # TODO: Сделать теорию под каждое задание
    # TODO: При нажатии отправляется ссылка на сайт с теорией
    await call.message.answer("Теория: ")
    await call.answer()


@ru_router.callback_query(RuCD.filter(F.action == RuCDAction.QUIZ_MODE))
async def quiz_mode_ru(call: CallbackQuery):
    # TODO: https://ru.stackoverflow.com/questions/1299118/aiogram-bot-quiz
    
    await call.message.answer("Выбери сколько заданий подряд ты хочешь решить", reply_markup=QUIZ_AMOUNT_KEYBOARD)
    await call.answer()


@ru_router.callback_query(F.data == "quiz_5_tasks")
async def quiz_5_tasks(call: CallbackQuery):
    right_answers = 0
    for i in range(5):
        task, answer = await get_b4_quiz()
        poll_message = await call.message.answer_poll(
            question="Выбери правильное ударение", options=[task[0], task[1]], 
            type='quiz', correct_option_id=answer, is_anonymous=False, 
            open_period=20
            )
        response = await poll_message.poll.wait()
        if response.option_ids[0] == answer:
            right_answers += 1
    await call.message.answer(f"Правильных ответов: {right_answers}")



@ru_router.callback_query(RuCD.filter(F.action == RuCDAction.THEME_MODE))
async def theme_mode_ru(call: CallbackQuery):
    # TODO: тренировка конкретного задания(1-26)
    await call.message.answer("Темы")
    await call.answer()


@ru_router.callback_query(RuCD.filter(F.action == RuCDAction.VARIANT_MODE))
async def variant_mode_ru(call: CallbackQuery):
    # TODO: сделать алгоритм генерации варианта
    await call.message.answer("Вариант")
    await call.answer()


@ru_router.callback_query(F.data == "modes_info")
async def modes_info_ru(call: CallbackQuery):
    # TODO: сделать описание каждого режима
    MODES_INFO_MESSAGE = ""
    await call.message.answer("Информация о режимах")
    await call.answer()


@ru_router.callback_query(F.data == "modes_close")
async def close_modes_ru(call: CallbackQuery):
    await call.message.delete()

# ! ниже тестовые функции
@ru_router.message(Command(commands='num'))
async def show_num_keyboard(message: Message):
    from structures.keyboards.ru_tasks_numbers_keyboard import KEYBOARD_1TO9
    await message.answer("Выбери номер задания", reply_markup=KEYBOARD_1TO9)


@ru_router.callback_query(F.data == "next_10to18")
async def ru_next_10to18(call: CallbackQuery):
    from structures.keyboards.ru_tasks_numbers_keyboard import KEYBOARD_10TO18
    await call.message.edit_reply_markup(reply_markup=KEYBOARD_10TO18)
    await call.answer()


@ru_router.callback_query(F.data == "back_10to18")
async def ru_back_10to18(call: CallbackQuery):
    from structures.keyboards.ru_tasks_numbers_keyboard import KEYBOARD_10TO18
    await call.message.edit_reply_markup(reply_markup=KEYBOARD_10TO18)
    await call.answer()


@ru_router.callback_query(F.data == "1to9")
async def ru_1to9(call: CallbackQuery):
    from structures.keyboards.ru_tasks_numbers_keyboard import KEYBOARD_1TO9
    await call.message.edit_reply_markup(reply_markup=KEYBOARD_1TO9)
    await call.answer()


@ru_router.callback_query(F.data == "19to27")
async def ru_19to27(call: CallbackQuery):
    from structures.keyboards.ru_tasks_numbers_keyboard import KEYBOARD_19TO27
    await call.message.edit_reply_markup(reply_markup=KEYBOARD_19TO27)
    await call.answer()