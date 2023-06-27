from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis
from asyncpg import connect
import asyncpg
import asyncio

from handlers.handlers import state_router
from middleware.init_user_db import InitUsersMeddleware
from middleware.state_contros_mdwr import InitUSers

TOKEN = "6095290433:AAE6t3nVcf9nNGOKdqVLZwobmy7hJuy-DWI"
async def start_app():
    redis: Redis = Redis(host="localhost")

    storage_redis: RedisStorage = RedisStorage(redis=redis, state_ttl=15)

    bot: Bot = Bot(TOKEN)
    dp: Dispatcher = Dispatcher(storage=storage_redis)
    pool = await asyncpg.create_pool(user='topevgn', password='1234', host='localhost', database='bot', command_timeout=60)
    dp.update.outer_middleware(InitUsersMeddleware(connect_db=pool))
    dp.update.outer_middleware(InitUSers())


    dp.include_router(state_router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start_app())
