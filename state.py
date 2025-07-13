# from aiogram.fsm.state import State, StatesGroup
# from aiogram import Router, F
# from aiogram import types
# from aiogram.filters import Command
# from keyboard.reply import do_u_like_bots
# from aiogram.fsm.context import FSMContext
# fsm_router = Router()

# class Form(StatesGroup):
#     name = State()
#     age = State()
#     like_bots = State()

# @fsm_router.message(Command('form'))
# async def cmd_start(message: types.Message, state: FSMContext):
#     await message.answer("Hi! What's your name?")
#     await state.set_state(Form.name)

# @fsm_router.message(Form.name)
# async def process_name(message:types.Message, state: FSMContext): 
#     await state.update_data(name=message.text)
#     await state.set_state(Form.age)
#     await message.answer(text='How old r u?')

# @fsm_router.message(Form.age, F.text.isdigit())
# async def process_age(message: types.Message, state: FSMContext): 
#     await state.update_data(age=message.text)
#     await state.set_state(Form.like_bots)
#     data = await state.get_data()
#     await message.answer(text=f'Nice to meet you, {data['name']}!\nDo you like tg bots?', reply_markup = do_u_like_bots)

# @fsm_router.message(Form.like_bots, F.text.casefold() == 'no')
# async def process_dont_like_write_bots(message: types.Message, state: FSMContext): 
#     await state.update_data(like_bots='no')
#     await message.answer(
#         'Not bad not terrible.\nSee you soon.',
#         reply_markup=types.ReplyKeyboardRemove()
#     )
#     await state.clear()

# @fsm_router.message(Form.like_bots, F.text.casefold() == 'yes')
# async def process_dont_like_write_bots(message: types.Message, state: FSMContext): 
#     await state.update_data(like_bots='yes')
#     await message.answer(
#         'Good enough.',
#         reply_markup=types.ReplyKeyboardRemove()
#     )
#     await state.clear()
    