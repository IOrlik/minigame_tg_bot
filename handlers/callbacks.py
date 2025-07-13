import aiogram 
from aiogram import Router, F 
from aiogram.types import CallbackQuery
from fight import Warrior, Archer, Mage, create_archer, create_mage, create_warrior, create_character
from Data import CHAR_AMOUNT, DataBase, characters
from fight import random_attacking_char, Character
from keyboard.inline import after_move_keyboard


callbacks_router = Router()


@callbacks_router.callback_query(F.data == 'warrior')
async def get_query(callback: CallbackQuery):
    id_user = callback.message.from_user.id
    DataBase[id_user] = DataBase.get(id_user, [])
    DataBase[id_user], text = create_character(id_user, 3)
    await callback.answer('')
    await callback.message.answer(text)

@callbacks_router.callback_query(F.data == 'mage')
async def get_query(callback: CallbackQuery):
    id_user = callback.message.from_user.id
    DataBase[id_user] = DataBase.get(id_user, [])
    DataBase[id_user], text = create_character(id_user, 2)
    await callback.answer('')
    await callback.message.answer(text)

@callbacks_router.callback_query(F.data == 'archer')
async def get_query(callback: CallbackQuery):
    id_user = callback.message.from_user.id
    DataBase[id_user] = DataBase.get(id_user, [])
    DataBase[id_user], text = create_character(id_user, 1)
    await callback.answer('')
    await callback.message.answer(text)


@callbacks_router.callback_query(F.data == 'startgame')
async def get_query(t: CallbackQuery):
    id_user = t.message.from_user.id
    if len(DataBase[id_user]) == 2 or len(DataBase[id_user]) == 3: 
        text = '<pre>==============-⚔ Бой начался ⚔-==============\n'
        if DataBase[id_user][2] != None:
            returned_data = random_attacking_char(DataBase[id_user][0], DataBase[id_user][1], DataBase[id_user][2])
            text += returned_data[1] + '\n' + returned_data[0]
        else: 
            returned_data = random_attacking_char(DataBase[id_user][0], DataBase[id_user][1])
            text += returned_data[1] + '\n' + returned_data[0]
        text += '</pre>'
        await t.answer('')
        await t.message.answer(text=text, parse_mode='HTML', reply_markup=after_move_keyboard)

@callbacks_router.callback_query(F.data == 'show_stats')
async def get_query(callback:CallbackQuery):
    id_user = callback.message.from_user.id
    text = '<pre>'
    for i in range(len(DataBase[id_user])):
        text += DataBase[id_user][i].show_stats() + '\n\n'
    text += '</pre>'
    await callback.answer('')
    await callback.message.answer(text=text, parse_mode='HTML')

@callbacks_router.callback_query(F.data == 'next_move')
async def get_query(t: CallbackQuery):
    id_user = t.message.from_user.id
    if not DataBase[id_user][0].is_alive() or not DataBase[id_user][1].is_alive() or not DataBase[id_user][2].is_alive():
        text = '<pre>==============-⚔ Бой закончился ⚔-==============\n'
        if not DataBase[id_user][0].is_alive():
            text += f'💀{DataBase[id_user][0].name()} умер'
        else: text += f'❤{DataBase[id_user][0].name()} жив'
        if not DataBase[id_user][1].is_alive():
            text += f'💀{DataBase[id_user][1].name()} умер' 
        else: text += f'❤{DataBase[id_user][1].name()} жив'     
        if not DataBase[id_user][2].is_alive():
            text += f'💀{DataBase[id_user][2].name()} умер'
        else: text += f'❤{DataBase[id_user][2].name()} жив'
        text += '\n'

    if len(DataBase[id_user]) == 2 or len(DataBase[id_user]) == 3 and (DataBase[id_user][0].is_alive() and DataBase[id_user][1].is_alive() and DataBase[id_user][2].is_alive()): 
        text = '<pre>\n'
        if DataBase[id_user][2] != None:
            returned_data = random_attacking_char(DataBase[id_user][0], DataBase[id_user][1], DataBase[id_user][2])
        else: 
            returned_data = random_attacking_char(DataBase[id_user][0], DataBase[id_user][1])
        text += returned_data[1] + '\n' + returned_data[0]
    text += '</pre>'
    await t.answer('')
    await t.message.answer(text=text, parse_mode='HTML', reply_markup=after_move_keyboard)


@callbacks_router.callback_query(F.data == 'test')
async def handle_test(t: CallbackQuery):
    await t.answer('ТОЛЬЯТТИ')
    await t.message.answer(text='Test')

@callbacks_router.callback_query(F.data == 'help')
async def handle_test(t: CallbackQuery):
    await t.answer('')
    await t.message.answer(text='Не, не буду помогать')



