from aiogram.fsm.state import State, StatesGroup
from aiogram import Router, F
from aiogram import types
from aiogram.filters import Command
from keyboard.reply import do_u_like_bots
from aiogram.fsm.context import FSMContext
from database import add_user, show_db
fsm_router = Router()

class Form(StatesGroup):
    name = State()
    age = State()
    like_bots = State()

@fsm_router.message(Command('form'))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Hi! What's your name?")
    await state.set_state(Form.name)

@fsm_router.message(Form.name)
async def process_name(message:types.Message, state: FSMContext): 
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer(text='How old r u?')

@fsm_router.message(Form.age, F.text.isdigit())
async def process_age(message: types.Message, state: FSMContext): 
    await state.update_data(age=message.text)
    await state.set_state(Form.like_bots)
    data = await state.get_data()
    await message.answer(text=f'Nice to meet you, {data['name']}!\nDo you like tg bots?', reply_markup = do_u_like_bots)

@fsm_router.message(Form.like_bots, F.text.casefold() == 'yes')
async def process_like_write_bots(message: types.Message, state: FSMContext) -> None: 
    await state.update_data(like_bots = 'yes')
    data = await state.get_data()
    add_user(
        user_id=message.from_user.id,
        name = data['name'],
        age = int(data['age']),
        like_bots = data['like_bots']
    )
    await state.clear()
    await message.reply(
        text="Cool, I'm too",
        reply_markup = types.ReplyKeyboardRemove()
    )
    print(show_db())


@fsm_router.message(Form.like_bots, F.text.casefold() == 'no')
async def process_like_write_bots(message: types.Message, state: FSMContext) -> None: 
    await state.update_data(like_bots = 'no')
    data = await state.get_data()
    add_user(
        user_id=message.from_user.id,
        name = data['name'],
        age = int(data['age']),
        like_bots = data['like_bots']
    )
    await state.clear()
    await message.reply(
        text="That's ok, I'll find you.",
        reply_markup = types.ReplyKeyboardRemove()
    )
    print(show_db())

