from aiogram import types, Dispatcher

import config
from create_bot import bot
from database import database
from keyboards import start_kb, admin_kb


async def start(message: types.Message):
    if message.from_user.id == config.ADMIN_ID:
        await message.answer('Сделать рассылку?', reply_markup=admin_kb.admin_start)
    await message.answer('Хотите подписаться на рассылку?', reply_markup=start_kb.subscription)


async def add_member(call: types.CallbackQuery):
    # Добавить пользователя в базу данных для рассылки сообщение
    database.add_member(str(call.from_user.id))
    await bot.send_message(call.from_user.id, 'Вы подписались. Для отписки введите команду /отписаться',
                           reply_markup=start_kb.unsubscribe)


async def unsubscribe(message: types.Message):
    # Удалить пользователя из базы данных
    database.delete_member(str(message.from_user.id))
    await message.answer('Вы отписались', reply_markup=start_kb.subscription)


def reg_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_callback_query_handler(add_member, text_contains='new_member')
    dp.register_message_handler(unsubscribe, commands=['отписаться'])
