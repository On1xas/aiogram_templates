from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis
from asyncpg import connect
import asyncpg

from handlers.handlers import state_router
from middleware.init_user_db import InitUsersMeddleware

TOKEN = "6095290433:AAE6t3nVcf9nNGOKdqVLZwobmy7hJuy-DWI"

redis: Redis = Redis(host="localhost")

storage_redis: RedisStorage = RedisStorage(redis=redis, state_ttl=15)

bot: Bot = Bot(TOKEN)
dp: Dispatcher = Dispatcher(storage=storage_redis)
pool = asyncpg.create_pool(user='topevgn', password='1234', host='localhost', database='bot', command_timeout=60)
dp.update.outer_middleware(InitUsersMeddleware(pool))


dp.include_router(state_router)


if __name__ == "__main__":
    dp.run_polling(bot)
