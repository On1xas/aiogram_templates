from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from database.database_service import RequestDB
import asyncpg

class InitUsersMeddleware(BaseMiddleware):
    def __init__(self, *args: object, connect_db: asyncpg.pool.Pool) -> None:
        super().__init__(*args)
        self.connection = connect_db

    async def __call__(self,
    handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
    event: TelegramObject,
    data: Dict[str, Any]
    ) -> Any:
        async with self.connection.acquire() as connect:
            data['db_connect'] = connect
            result = await handler(event, data)
            return result