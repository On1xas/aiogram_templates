from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis

from handlers.handlers import state_router

TOKEN = "6095290433:AAE6t3nVcf9nNGOKdqVLZwobmy7hJuy-DWI"

redis: Redis = Redis(host="localhost")

storage_redis: RedisStorage = RedisStorage(redis=redis, state_ttl=15)

bot: Bot = Bot(TOKEN)
dp: Dispatcher = Dispatcher(storage=storage_redis)


dp.include_router(state_router)


if __name__ == "__main__":
    dp.run_polling(bot)
