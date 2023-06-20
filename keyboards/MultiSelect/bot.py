from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.handler import multi_select_router

TOKEN = "6095290433:AAE6t3nVcf9nNGOKdqVLZwobmy7hJuy-DWI"
storage: MemoryStorage = MemoryStorage()
bot: Bot = Bot(TOKEN)
dp: Dispatcher = Dispatcher()


dp.include_router(multi_select_router)


if __name__ == "__main__":
    dp.run_polling(bot)