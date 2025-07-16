import aiogram 
from aiogram import Router, F
from aiogram.filters import or_f
from aiogram.types import CallbackQuery
from fight import Warrior, Archer, Mage, create_archer, create_mage, create_warrior, create_character
from Data import CHAR_AMOUNT, DataBase, fantasy_archer_names, fantasy_mage_names, fantasy_warrior_names
from fight import random_attacking_char, Character
from keyboard.inline import after_move_keyboard, after_end_keyboard, characters_spawn

callbacks_router = Router()


# @callbacks_router.callback_query(or_f(F.data == 'mage', F.data == 'warrior', F.data == 'archer'))
# async def get_query(callback: CallbackQuery):
#     id_user = callback.message.from_user.id
#     DataBase[id_user] = DataBase.get(id_user, [])
#     print(F.data)
#     if F.data == 'mage':
#         DataBase[id_user], text = create_character(id_user, 2)
#     elif F.data == 'archer': 
#         DataBase[id_user], text = create_character(id_user, 1)
#     else: 
#         DataBase[id_user], text = create_character(id_user, 3)
#     await callback.answer('')
#     print(DataBase[id_user])
#     await callback.message.answer(text)



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

@callbacks_router.callback_query(F.data == 'knight')
async def get_query(callback: CallbackQuery):
    id_user = callback.message.from_user.id
    DataBase[id_user] = DataBase.get(id_user, [])
    DataBase[id_user], text = create_character(id_user, 4)
    await callback.answer('')
    await callback.message.answer(text)

@callbacks_router.callback_query(or_f(F.data == 'create', F.data == 'create_new'))
async def command_create_handler(t: CallbackQuery) -> None:
    id_user = t.message.from_user.id  
    DataBase[id_user] = []
    text = f'🤔 Создай разных персонажей (необязательно разных классов)\n❗ Максимум можно создать всего 3 персонажа'
    await t.answer('')
    await t.message.answer(text, reply_markup=characters_spawn)

@callbacks_router.callback_query(or_f(F.data == 'startgame'))
async def get_query(t: CallbackQuery):
    await t.answer('')
    await t.message.edit_text(f'{t.message.text}', parse_mode = 'HTML')
    id_user = t.message.from_user.id
    if len(DataBase[id_user]) == 3:  
        text = '<pre>==-⚔ Бой начался ⚔-==\n'
        text += random_attacking_char(DataBase[id_user][0], DataBase[id_user][1], DataBase[id_user][2])
        text += '</pre>'
        await t.message.answer(text=text, parse_mode='HTML', reply_markup=after_move_keyboard)
    else: 
        text = 'Вам надо создать 3 персонажа'
        await t.message.answer(text=text, parse_mode='HTML')
    


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

    elif len(DataBase[id_user]) == 3:
        text = '<pre>\n'
        text += random_attacking_char(DataBase[id_user][0], DataBase[id_user][1], DataBase[id_user][2])
        text += '</pre>'
        await t.message.answer(text=text, parse_mode='HTML', reply_markup=after_move_keyboard)
    



