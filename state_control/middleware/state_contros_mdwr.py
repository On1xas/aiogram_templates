from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, CallbackQuery
from aiogram.fsm.context import FSMContext
from FSM.fsm import FSMuser_state

from keyboards.kb import start_kb

class StateControsUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        fsm : FSMContext = data['state']
        print(data['raw_state'])
        if data['raw_state'] is None:
            print("BLOCKED")
            await fsm.set_state(FSMuser_state.stage2)
            await event.message.answer(text=f"Main Menu {await fsm.get_state()}", reply_markup=start_kb())
            await event.message.delete()
        else:
            print("NOT BLOCKED")
            result = await handler(event, data)
            return result