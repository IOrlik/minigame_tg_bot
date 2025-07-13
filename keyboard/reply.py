from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/about'), KeyboardButton(text='/start')], 
        [KeyboardButton(text='/help'), KeyboardButton(text='/create')],
        [KeyboardButton(text = '/remove_keyboard')]
    ],
    resize_keyboard=True 
)

do_u_like_bots = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = 'yes'), KeyboardButton(text='no')]
    ]
)