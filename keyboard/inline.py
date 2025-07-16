from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = "Создать воина", url = 'https://gpu.userbenchmark.com/')],
        [InlineKeyboardButton(text = 'Не создавать воина', url = 'https://gpu.userbenchmark.com/')]
    ]
)

about_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = '📖 GitHub', url = 'https://github.com/IOrlik/minigame_tg_bot#')],
        [InlineKeyboardButton(text = '📖 Документация', url = 'https://docs.aiogram.dev/en/v3.21.0/')],
        [InlineKeyboardButton(text = '📖 Помощь', callback_data='help')]
    ]
)


characters_spawn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = '⚔ Создать Воина', callback_data='warrior'), InlineKeyboardButton(text = '🔮 Создать Мага', callback_data='mage')],
        [InlineKeyboardButton(text = '🏹 Создать Лучника', callback_data='archer'), InlineKeyboardButton(text='🛡 Создать Рыцаря', callback_data = 'knight')],
        [InlineKeyboardButton(text = '⚔ Начать битву', callback_data = 'startgame')]        
    ]
)

after_move_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='⏭ Следующий ход', callback_data='next_move'), 
        InlineKeyboardButton(text='📖 Статистика', callback_data='show_stats')]
    ]
)

after_end_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🆕 Новая игра с новыми персонажами', callback_data='create_new')], 
        [InlineKeyboardButton(text='📖 Статистика', callback_data='show_stats')]
    ]
)

testkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = "Test", callback_data = 'test')],
    ]
)