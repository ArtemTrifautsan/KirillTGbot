from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

confirm = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Да'), KeyboardButton(text='Нет')]],
    resize_keyboard=True
)

admin_start = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='/сделать_рассылку')]],
    resize_keyboard=True
)
