from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, PollAnswer, Poll
from typing import List
from structures.keyboards.ru_practice_types_keyboard import RU_PRACTICE_TYPES_KEYBOARD
from structures.keyboards.quiz_keyboard import QUIZ_KEYBOARD
from structures.keyboards.ru_tasks_numbers_keyboard import KEYBOARD_1TO9
from structures.keyboards.ru_tasks_numbers_keyboard import KEYBOARD_10TO18
from structures.keyboards.ru_tasks_numbers_keyboard import KEYBOARD_19TO27
from structures.callback_data.ru_callback_data import RuCD, RuCDAction
from structures.callback_data.ru_task_numbers_callback_data import RuTaskNumberCD, RuTaskNumberCDAction
from src.db.tasks_db.static.ru_b4 import get_b4_quiz
from src.db.tasks_db.static.ru_b5 import get_b5_quiz

ru_router = Router(name='ru')

class UserPollAnswer():
    # TODO: как классы в python хранят значения
    userAnswers:List[int] = []
    rightAnsers:List[int] = []

class TaskNumber():
    # TODO: 
    taskNumber: RuTaskNumberCDAction = RuTaskNumberCDAction.one

userPollAnswer = UserPollAnswer()
taskNumber = TaskNumber()


@ru_router.message(F.text=="Русский язык")
async def training_types(message: Message):
    await message.answer(text="Выбери режим тренировки📊", reply_markup=RU_PRACTICE_TYPES_KEYBOARD)


@ru_router.callback_query(RuCD.filter(F.action == RuCDAction.THEORY_MODE))
async def theory_mode_ru(call: CallbackQuery):
    # TODO: Сделать теорию под каждое задание
    # TODO: При нажатии отправляется ссылка на сайт с теорией
    # TODO: сделать документацию по каждому заданию
    await call.message.answer("Теория: ")
    await call.answer()


@ru_router.callback_query(RuCD.filter(F.action == RuCDAction.QUIZ_MODE))
async def quiz_mode_ru(call: CallbackQuery):
    await call.message.answer("Выбери задание, которое хочешь тренировать", reply_markup=KEYBOARD_1TO9)
    # await make_quiz(call, RuTaskNumberCDAction.five)
    await call.answer()


@ru_router.poll_answer()
async def poll_answer_handler(poll_answer: PollAnswer):
    user_answer = poll_answer.option_ids
    userPollAnswer.userAnswers.append(user_answer)
    if len(userPollAnswer.rightAnsers) - len(user_answer) == 1:
        userPollAnswer.userAnswers.append([-1])
    # !
    print(userPollAnswer.rightAnsers)
    print(userPollAnswer.userAnswers)


async def make_quiz(call: CallbackQuery, task_type: RuTaskNumberCDAction) -> None:
    # ! poetry run python src\bot\__main__.py
    # TODO: сделать квиз на все задания по орфографии + задание на средства выразительности
    taskNumber = task_type
    match task_type:
        case RuTaskNumberCDAction.four:
            await make_task_4(call)
        case RuTaskNumberCDAction.five:
            await make_task_5(call)
    
    await call.message.answer("Выбери действие", reply_markup=QUIZ_KEYBOARD)


async def make_task_4(call: CallbackQuery) -> None:
    task, answer = await get_b4_quiz()
    userPollAnswer.rightAnsers.append([answer])
    await call.message.answer_poll(
        question=f"⌛️Выбери правильное ударение", options=[task[0], task[1]], 
        type='quiz', correct_option_id=answer, is_anonymous=False, 
        open_period=20
        )


async def make_task_5(call: CallbackQuery) -> None:
    try:
        task, right_answer, answers = await get_b5_quiz()
        userPollAnswer.rightAnsers.append([right_answer])
        await call.message.answer_poll(
            question=f"⌛️{task}", options=answers, 
            type='quiz', correct_option_id=right_answer, is_anonymous=False, 
            open_period=20
            )
    except Exception as e:
        print(e)
        print(task)


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

#! Повторный квиз
@ru_router.callback_query(F.data == "more_quiz")
async def more_quiz(call: CallbackQuery):
    await make_quiz(call, RuTaskNumberCDAction.five)


@ru_router.callback_query(F.data == "quit_quiz")
async def quit_quiz(call: CallbackQuery):
    right_ans = userPollAnswer.rightAnsers
    user_ans = userPollAnswer.userAnswers
    all_ans = len(right_ans)
    right_user_ans = len([1 for i in range(all_ans) if right_ans[i] == user_ans[i]])
    print(right_ans)
    print(user_ans)
    userPollAnswer.rightAnsers.clear()
    userPollAnswer.userAnswers.clear()
    await call.answer(f"Правильно выполнено {right_user_ans}/{all_ans}", show_alert=True)


#! Движения клавиатуры
@ru_router.callback_query(F.data == "next_10to18")
async def ru_next_10to18(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=KEYBOARD_10TO18)
    await call.answer()


@ru_router.callback_query(F.data == "back_10to18")
async def ru_back_10to18(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=KEYBOARD_10TO18)
    await call.answer()


@ru_router.callback_query(F.data == "1to9")
async def ru_1to9(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=KEYBOARD_1TO9)
    await call.answer()


@ru_router.callback_query(F.data == "19to27")
async def ru_19to27(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=KEYBOARD_19TO27)
    await call.answer()


#! Обработка номеров заданий
@ru_router.callback_query(RuTaskNumberCD.filter(F.action == RuTaskNumberCDAction.one))
async def ru_one(call: CallbackQuery):
    await call.message.answer("Задание 1")


@ru_router.callback_query(RuTaskNumberCD.filter(F.action == RuTaskNumberCDAction.two))
async def ru_two(call: CallbackQuery):
    ...


@ru_router.callback_query(RuTaskNumberCD.filter(F.action == RuTaskNumberCDAction.three))
async def ru_three(call: CallbackQuery):
    ...


@ru_router.callback_query(RuTaskNumberCD.filter(F.action == RuTaskNumberCDAction.four))
async def ru_four(call: CallbackQuery):
    await make_quiz(call, RuTaskNumberCDAction.four)
    await call.answer()


@ru_router.callback_query(RuTaskNumberCD.filter(F.action == RuTaskNumberCDAction.five))
async def ru_five(call: CallbackQuery):
    await make_quiz(call, RuTaskNumberCDAction.five)
    await call.answer()