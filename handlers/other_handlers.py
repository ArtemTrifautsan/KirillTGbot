from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove

import config
from create_bot import bot
from database import database
from keyboards import start_kb, admin_kb


async def start(message: types.Message):
    if message.from_user.id == config.ADMIN_ID:
        await bot.send_message(message.from_user.id, text='Сделать рассылку?', reply_markup=admin_kb.admin_start)
    else:
        await bot.send_message(message.from_user.id, text='Хотите подписаться на рассылку?',
                               reply_markup=start_kb.subscription)


async def new_member(message: types.Message):
    # Функция добавляет в базу данных нового участника сообщества
    database.add_member(message.from_user.id, message.chat.id)    # Добавить участника в базу данных
    await message.answer(f'Здравствуй, {message.from_user.first_name}. Подписаться на рассылку можно в личных '
                         f'сообщениях бота (меня).', reply_markup=ReplyKeyboardRemove())


async def left_member(message: types.Message):
    # Функция добавляет в базу данных нового участника сообщества
    database.delete_member(message.from_user.id)    # Добавить участника в базу данных
    await message.answer(f'Участник с id {message.from_user.id} удалён')


def reg_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(new_member, content_types=types.ContentType.NEW_CHAT_MEMBERS)
    dp.register_message_handler(left_member, content_types=types.ContentType.LEFT_CHAT_MEMBER)
