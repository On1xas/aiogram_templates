import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from aiogram.types import Message

from handlers.handler import multi_select_router

async def main():
    TOKEN = "6095290433:AAE6t3nVcf9nNGOKdqVLZwobmy7hJuy-DWI"
    storage: MemoryStorage = MemoryStorage()
    bot: Bot = Bot(TOKEN)
    dp: Dispatcher = Dispatcher(storage=storage)

    @dp.message(CommandStart())
    async def st(message: Message):
        await message.answer(text="H")

    dp.include_router(multi_select_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())