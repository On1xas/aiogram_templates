from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from middleware.state_contros_mdwr import StateControsUserMiddleware


from FSM.fsm import FSMuser_state
from keyboards.kb import start_kb

state_router = Router()
state_router.callback_query.outer_middleware(StateControsUserMiddleware())

@state_router.message(CommandStart(), StateFilter(default_state))
async def start(message: Message, state: FSMContext):
    await message.answer(text=f"Hello, your state {await state.get_state()}", reply_markup=start_kb())


@state_router.callback_query(Text(text="TEST"))
async def test_cb(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMuser_state.stage1)
    await callback.message.edit_text(text=f"Вы еще в state: {await state.get_state()}", reply_markup=start_kb())
