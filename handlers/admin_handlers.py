from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

import config
from create_bot import bot
from keyboards import admin_kb


class FSMDistribution(StatesGroup):
    msg = State()
    groups = State()
    confirm = State()


async def make_distribution(message: types.Message):
    if message.from_user.id == config.ADMIN_ID:
        await FSMDistribution.msg.set()
        await message.answer('Что будем рассылать?')
    else:
        await bot.send_message(message.from_user.id, 'Нет такой команды')


async def text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message'] = message
    await FSMDistribution.next()
    await message.answer('Перечислите id групп через запятую без пробела')


async def groups(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['groups_id'] = message.text
    await FSMDistribution.next()
    await message.answer('Подтвердить отправку?', reply_markup=admin_kb.confirm)


async def confirming(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        async with state.proxy() as data:
            await message.answer(f"{data['message']}/n/n{data['group_id']}")
        await message.answer('Рассылка отправлена')
    else:
        await message.answer('Рассылка отменена')
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(make_distribution, commands=['сделать_рассылку'], state=None)
    dp.register_message_handler(text, state=FSMDistribution.msg)
    dp.register_message_handler(groups, state=FSMDistribution.groups)
    dp.register_message_handler(confirming, state=FSMDistribution.confirm)
