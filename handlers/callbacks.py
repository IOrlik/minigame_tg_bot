import aiogram 
from aiogram import Router, F
from aiogram.filters import or_f
from aiogram.types import CallbackQuery
from fight import Warrior, Archer, Mage, create_archer, create_mage, create_warrior, create_character
from Data import CHAR_AMOUNT, DataBase, fantasy_archer_names, fantasy_mage_names, fantasy_warrior_names
from fight import random_attacking_char, Character
from keyboard.inline import after_move_keyboard, after_end_keyboard, characters_spawn


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

@callbacks_router.callback_query(or_f(F.data == 'create'))
async def command_start_handler(t: CallbackQuery) -> None:
    text = f'Выбирайте какого персонажа хотите создать (Вы должны создать 2 или 3 разных персонажа, необязательно разных классов)'
    await t.answer('')
    await t.message.answer(text, reply_markup=characters_spawn)

@callbacks_router.callback_query(or_f(F.data == 'startgame'))
async def get_query(t: CallbackQuery):
    await t.answer('')
    id_user = t.message.from_user.id
    if len(DataBase[id_user]) == 2 or len(DataBase[id_user]) == 3:  
        text = '<pre>==-⚔ Бой начался ⚔-==\n'
        if DataBase[id_user][2] != None:
            returned_data = random_attacking_char(DataBase[id_user][0], DataBase[id_user][1], DataBase[id_user][2])
            text += returned_data[1] + '\n' + returned_data[0]
        else: 
            returned_data = random_attacking_char(DataBase[id_user][0], DataBase[id_user][1])
            text += returned_data[1] + '\n' + returned_data[0]
        text += '</pre>'
        await t.message.answer(text=text, parse_mode='HTML', reply_markup=after_move_keyboard)

@callbacks_router.callback_query(F.data == 'show_stats')
async def get_query(callback:CallbackQuery):
    id_user = callback.message.from_user.id
    text = '<pre>'
    print(DataBase[id_user])
    for i in range(len(DataBase[id_user])):
        text += DataBase[id_user][i].show_stats() + '\n\n'
    text += '</pre>'
    await callback.answer('')
    await callback.message.answer(text=text, parse_mode='HTML')

@callbacks_router.callback_query(F.data == 'next_move')
async def get_query(t: CallbackQuery):
    await t.message.edit_text(text=f'<pre>{t.message.text}</pre>', parse_mode = 'HTML')
    id_user = t.message.from_user.id
    await t.answer('')
    if not DataBase[id_user][0].is_alive() or not DataBase[id_user][1].is_alive() or not DataBase[id_user][2].is_alive():
        text = '<pre>==-⚔ Бой закончился ⚔-==\n'
        for i in range(len(DataBase[id_user])):
            if not DataBase[id_user][i].is_alive():
                text += f'💀{DataBase[id_user][i].name} умер\n'
            else: text += f'❤{DataBase[id_user][i].name} жив\n'
        text += '</pre>'
        text += '\n'
        await t.message.answer(text=text, parse_mode='HTML', reply_markup=after_end_keyboard)

    elif len(DataBase[id_user]) == 2 or len(DataBase[id_user]) == 3:
        text = '<pre>\n'
        if DataBase[id_user][2] != None:
            returned_data = random_attacking_char(DataBase[id_user][0], DataBase[id_user][1], DataBase[id_user][2])
        else: 
            returned_data = random_attacking_char(DataBase[id_user][0], DataBase[id_user][1])
        text += returned_data[1] + '\n' + returned_data[0]
        text += '</pre>'
        await t.message.answer(text=text, parse_mode='HTML', reply_markup=after_move_keyboard)
    



