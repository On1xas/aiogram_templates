from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from aiogram.fsm.context import FSMContext

from lexicon.lexicon import LEXICON_RU_MULTI_SELECT_BUTTON, LEXICON_RU_BUTTON


async def kb_time_to_sign(state: FSMContext):
    kb = InlineKeyboardBuilder()
    selected = await state.get_data()
    main_button = []
    print(selected)   
    for time in LEXICON_RU_MULTI_SELECT_BUTTON['times_to_sign']:
        if selected and time in selected['select_button'] and LEXICON_RU_MULTI_SELECT_BUTTON['times_to_sign'].count(time)%2==1:
            main_button.append(InlineKeyboardButton(text=f"[{time}]", callback_data=time))
        else:
            main_button.append(InlineKeyboardButton(text=f"{time}", callback_data=time))
    kb.row(*main_button, width=5)
    kb.row(InlineKeyboardButton(text=LEXICON_RU_BUTTON["time_selected"], callback_data="time_selected"), width=1)
    return kb.as_markup()