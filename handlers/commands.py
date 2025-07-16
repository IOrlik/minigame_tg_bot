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
    text = f'📕 Вы открыли меню, теперь у вас есть клавиатура с основными командами этого ТГ бота: \n'
    await message.answer(text, reply_markup=reply_kb)

@command_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    text = f'👋 Привет, я ТГ бот миниигра, где ты можешь создать своих персонажей и следить за ходом их битвы!\n🤔 Чтобы продолжить напишите команду /create'
    await message.answer(text)

@command_router.message(Command("about"))
async def command_start_handler(message: Message) -> None:
    text = f'📕 С помощью кнопок ниже ты сможешь больше узнать обо мне!'
    await message.answer(text, reply_markup=about_kb)


@command_router.message(Command("create"))
async def command_start_handler(message: Message) -> None:
    text = f'🤔 Создай разных персонажей (необязательно разных классов)\n❗ Максимум можно создать всего 3 персонажа'
    await message.answer(text, reply_markup=characters_spawn)

@command_router.message(Command("help"))
async def command_start_handler(message: Message) -> None:
    text = f'📕 Через /menu можно получить быстрый доступ ко всем командам\n📗 Через /about ты можешь узнать больше о боте\n📘 Через /create ты можешь создать персонажей и начать игру\n📙 Через /remove_keyboard можно убрать клавиатуру'
    await message.answer(text)

@command_router.message(Command('remove_keyboard'))
async def command_start_handler(message: Message) -> None: 
    text = '✅ Клавиатура убрана'
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