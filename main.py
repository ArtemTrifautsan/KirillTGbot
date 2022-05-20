from aiogram.utils import executor

from create_bot import dp
from handlers import other_handlers


async def on_startup(dp):
    # Выполнить при запуске бота
    print('+++Бот включен+++')


async def on_shutdown(dp):
    # Выполнить при выключении бота
    print('---Бот отключился---')


# Зарегистрировать хендлеры
other_handlers.reg_handlers(dp)


# Запуск бота в формате polling
executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
