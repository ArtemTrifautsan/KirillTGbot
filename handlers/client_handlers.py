from aiogram import Dispatcher, types

import config
from create_bot import bot
from database import database
from keyboards import admin_kb, start_kb


async def subs_to_dist(call: types.CallbackQuery):
    # Добавить пользователя в базу данных для рассылки сообщение
    database.subs(call.from_user.id)
    await bot.send_message(call.from_user.id, 'Вы подписались. Для отписки введите команду /отписаться',
                           reply_markup=start_kb.unsubscribe)


async def unsubs_to_dist(message: types.Message):
    # Добавить пользователя в базу данных для рассылки сообщение
    database.unsubs(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Вы отписались', reply_markup=start_kb.subscription)


def reg_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(subs_to_dist, text_contains='new_member')
    dp.register_message_handler(unsubs_to_dist, commands=['отписаться'])
