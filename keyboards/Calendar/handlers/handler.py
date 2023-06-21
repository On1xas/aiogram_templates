import datetime
from copy import deepcopy

from aiogram import Router
from aiogram.filters import CommandStart, Text
from aiogram.types import CallbackQuery, Message

from database.database import user_db, user_dict_template
from filters.filter import FilterCalendar, FilterDateCalendar
from keyboards.keyboard import kb_calendar

router_calendar: Router = Router()


@router_calendar.callback_query(FilterCalendar())
async def next_back_month(callback: CallbackQuery):
    if callback.data == "next_month":
        user_db[callback.from_user.id]["month"] += 1
        if user_db[callback.from_user.id]["month"] > 12:
            user_db[callback.from_user.id]["month"] = 1
            user_db[callback.from_user.id]["year"] += 1
    if callback.data == "back_month":
        user_db[callback.from_user.id]["month"] -= 1
        if user_db[callback.from_user.id]["month"] <= 0:
            user_db[callback.from_user.id]["month"] = 12
            user_db[callback.from_user.id]["year"] -= 1
    await callback.message.edit_text(text=callback.message.text,
                                     reply_markup=kb_calendar(month=user_db[callback.from_user.id]["month"], year=user_db[callback.from_user.id]["year"]))

@router_calendar.callback_query(Text(text="empty"))
async def empty_calendar(callback: CallbackQuery):
    await callback.answer()

@router_calendar.callback_query(FilterDateCalendar())
async def date_calendar(callback: CallbackQuery):
    await callback.answer(text=callback.data)

@router_calendar.message(CommandStart())
async def start(message: Message):
    if message.from_user.id not in user_db:
        user_db[message.from_user.id] = deepcopy(user_dict_template)
        user_db[message.from_user.id]["month"] = datetime.datetime.now().month
        user_db[message.from_user.id]["year"] = datetime.datetime.now().year
    await message.answer(text="Hello Calendar", reply_markup=kb_calendar())
