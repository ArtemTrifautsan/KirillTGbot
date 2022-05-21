from aiogram.utils import executor

import config
from create_bot import dp
from database import database
from handlers import other_handlers, admin_handlers, client_handlers


async def on_startup(dp):
    # Выполнить при запуске бота
    print('+++Бот включен+++')


async def on_shutdown(dp):
    # Выполнить при выключении бота
    print('---Бот отключился---')


# Зарегистрировать хендлеры
admin_handlers.register_handlers(dp)
client_handlers.reg_handlers(dp)
other_handlers.reg_handlers(dp)

# Создать базу данных если её нет
database.create_db(config.ADMIN_ID, -1001556943381)


# Запуск бота в формате polling
executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
