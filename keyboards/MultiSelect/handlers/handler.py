from aiogram import Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery

from fsm.fsm import FSM_MultiSelect
from keyboards.keyboards import kb_time_to_sign

multi_select_router: Router = Router()

# Этот хэндлер будет срабатывать на команду /start вне состояний
# и предлагать перейти к заполнению анкеты, отправив команду /fillform
@multi_select_router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(text='Тут мы тестим мульти селект', reply_markup= await kb_time_to_sign(state=state))
    await state.update_data(select_button=[])
    print(await state.get_data())
    await state.set_state(FSM_MultiSelect.stage1)

# Этот хэндлер будет срабатывать на команду /fillform
# и переводить бота в состояние ожидания ввода имени
@multi_select_router.callback_query(lambda callback: callback.data == "time_selected", StateFilter(FSM_MultiSelect.stage1))
async def process_fillform_command(callback: CallbackQuery, state: FSMContext):
    select_button = await state.get_data()
    select_button=sorted(list(set(select_button['select_button'])))
    text=", ".join(select_button)
    await callback.answer(text=f'Вы выбрали {text}')


@multi_select_router.callback_query(StateFilter(FSM_MultiSelect.stage1))
async def select_time(callback: CallbackQuery, state: FSMContext):
    select_button: dict[str, list] = await state.get_data()
    if callback.data not in select_button['select_button']:
        select_button['select_button'].append(callback.data)
    else:
        select_button['select_button'].remove(callback.data)
    await state.set_data(select_button)
    select_button=sorted(list(set(select_button['select_button'])))
    text=", ".join(select_button)
    await callback.message.edit_text(text=f"Ваш выбор: {text}", reply_markup= await kb_time_to_sign(state=state))





