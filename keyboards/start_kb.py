from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from keyboards import callback_datas

subscription = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='Подписаться на рассылку',
                                           callback_data=callback_datas.subscribe_callback.new(type_='new_member'))]],
)

unsubscribe = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='/отписаться')]],
    resize_keyboard=True
)
