from aiogram.fsm.state import StatesGroup, State


class FSM_MultiSelect(StatesGroup):
    stage1 = State()
    stage2 = State()

    