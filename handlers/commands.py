from aiogram import Router 
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from keyboard.inline import inline_kb, about_kb, characters_spawn, testkb
from Data import CHAR_AMOUNT
from keyboard.reply import reply_kb
from aiogram.types import ReplyKeyboardRemove
command_router = Router()


@command_router.message(Command("menu"))
async def command_start_handler(message: Message) -> None:
    text = f'Вы открыли меню'
    await message.answer(text, reply_markup=reply_kb)

@command_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    text = f'*очень красивый текст, который очень красиво описывает то как пользователь шедеврально нажал на кнопку, запустив игру*\nДля продолжения используйте команду create'
    await message.answer(text)

@command_router.message(Command("about"))
async def command_start_handler(message: Message) -> None:
    text = f'обо мне'
    await message.answer(text, reply_markup=about_kb)


@command_router.message(Command("create"))
async def command_start_handler(message: Message) -> None:
    text = f'Выбирайте какого персонажа хотите создать (Вы должны создать 2 или 3 разных персонажа, необязательно разных классов)'
    await message.answer(text, reply_markup=characters_spawn)

@command_router.message(Command("help"))
async def command_start_handler(message: Message) -> None:
    text = f'Через /menu можно получить быстрый доступ ко всем командам'
    await message.answer(text)

@command_router.message(Command('remove_keyboard'))
async def command_start_handler(message: Message) -> None: 
    text = 'a'
    await message.answer(text, reply_markup=ReplyKeyboardRemove())



# @command_router.message(Command("create_warrior"))
# async def command_start_handler(message: Message, char_amount = char_amount) -> None:
#     print(CHAR_AMOUNT)
#     if CHAR_AMOUNT >= 3: 
#         text = f'Достигнуто максимальное кол-во персонажей'
#     else: 
#         create_warrior(100, 50, 'Warrior')
#         CHAR_AMOUNT += 1
#         text = f'Вы создали воина'
#     await message.answer(text)



# @command_router.message(F.text.lower() == 'привет')
# async def command_start_handler(message: Message) -> None:
#     text = f'Не'
#     await message.answer(text)

# @command_router.message(F.text.lower() == 'пока')
# async def command_start_handler(message: Message) -> None:
#     text = f'Пока'
#     await message.answer(text)

# @command_router.message(F.text.contains('❤'))
# async def command_start_handler(message: Message) -> None:
#     text = f'Ура сердце'
#     await message.answer(text)

# @command_router.message(F.sticker)
# async def command_start_handler(message: Message) -> None:
#     text = f'тупа топ стикер'
#     await message.answer(text)

# @command_router.message(F.photo)
# async def command_start_handler(message: Message) -> None:
#     text = f'тупа топ фотка'
#     await message.answer(text)










# @command_router.message()
# async def echo_message(message: Message) -> None:
#     try:
#         await message.reply(text=message.text)
#     except TypeError:
#         await message.answer("Nice try!")