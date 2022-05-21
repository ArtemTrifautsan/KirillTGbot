import time

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ContentType

import config
from create_bot import bot
from distribution import distribution
from keyboards import admin_kb


class FSMDistribution(StatesGroup):
    msg = State()
    groups = State()
    confirm = State()


# Начало рассылки
async def make_distribution(message: types.Message):
    if message.from_user.id == config.ADMIN_ID:
        await FSMDistribution.msg.set()
        await message.answer('Что будем рассылать?')
    else:
        await bot.send_message(message.from_user.id, 'Нет такой команды')


# Получить сообщение для рассылки
async def text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message'] = message
    await FSMDistribution.next()
    await message.answer('Перечислите id групп через запятую без пробела')


# Получить список групп для рассылки
async def groups(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['groups_id'] = message.text
    await FSMDistribution.next()
    await message.answer('Подтвердить отправку?', reply_markup=admin_kb.confirm)


# Получить подтверждение рассылки
async def confirming(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        async with state.proxy() as data:
            list_members = distribution(data['groups_id'])

            for item in list_members:
                if data['message'].text is not None:
                    await bot.send_message(item[0], data['message'].text)
                elif data['message'].document is not None:
                    await bot.send_document(chat_id=item[0], document=data['message'].document.file_id,
                                            caption=data['message'].text)
                elif data['message'].photo is not None:
                    await bot.send_photo(chat_id=item[0], photo=data['message'].photo[-1].file_id,
                                         caption=data['message'].text)

                await bot.send_message(config.ADMIN_ID, f'Сообщение рассылки отправлено пользователю {item[0]}')

                time.sleep(1)

        await message.answer('Рассылка выполнена', reply_markup=admin_kb.admin_start)
    else:
        await message.answer('Рассылка отменена', reply_markup=admin_kb.admin_start)
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(make_distribution, commands=['сделать_рассылку'], state=None)
    dp.register_message_handler(text, content_types=[ContentType.ANY], state=FSMDistribution.msg)
    dp.register_message_handler(groups, state=FSMDistribution.groups)
    dp.register_message_handler(confirming, state=FSMDistribution.confirm)
