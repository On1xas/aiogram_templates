from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery

from fsm.fsm import FSM_MultiSelect
from keyboards.keyboards import kb_time_to_sign

multi_select_router: Router = Router()

@multi_select_router.message(CommandStart())
async def start(message: Message):
    print("START")
    await message.answer(text='Я не завис')

@multi_select_router.message(Command(commands=["sing"]), StateFilter(default_state))
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(text='Тут мы тестим мульти селект', reply_markup=await kb_time_to_sign(state=state))
    await state.update_data(select_button=[])
    await state.set_state(FSM_MultiSelect.stage1)


@multi_select_router.callback_query(lambda callback: callback.data == "time_selected", StateFilter(FSM_MultiSelect.stage1))
async def process_multi_select(callback: CallbackQuery, state: FSMContext):
    select_button = await state.get_data()
    text = ", ".join(sorted(list(select_button['select_button'])))
    await state.clear()
    await callback.answer(text=f'Вы выбрали {text}')
    await callback.message.delete()

@multi_select_router.callback_query(StateFilter(FSM_MultiSelect.stage1))
async def select_time(callback: CallbackQuery, state: FSMContext):
    select_button: dict[str, list] = await state.get_data()
    if callback.data not in select_button['select_button']:
        select_button['select_button'].append(callback.data)
    else:
        select_button['select_button'].remove(callback.data)
    await state.set_data(select_button)
    text = ", ".join(sorted(list(select_button['select_button'])))
    await callback.message.edit_text(text=f"Ваш выбор: {text}", reply_markup=await kb_time_to_sign(state=state))
