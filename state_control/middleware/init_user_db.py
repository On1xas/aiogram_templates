from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

class InitUsersMeddleware(BaseException):
    def __init__(self, *args: object, connect_db) -> None:
        super().__init__(*args)
        self.connection = connect_db

    async def __call__(self, 
    handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
    event: TelegramObject,
    data: Dict[str, Any]
    ) -> Any:


        result = await handler(event, data)
        return result