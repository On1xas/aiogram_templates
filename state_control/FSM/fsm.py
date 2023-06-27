from aiogram.fsm.state import State, StatesGroup


class FSMuser_state(StatesGroup):
    stage1 = State()
    stage2 = State()