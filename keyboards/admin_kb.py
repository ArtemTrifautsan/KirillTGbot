from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура потверждения отправки рассылки
confirm = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Да'), KeyboardButton(text='Нет')]],
    resize_keyboard=True
)

# Клавиатура старта для админа
admin_start = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='/сделать_рассылку')]],
    resize_keyboard=True
)
