from aiogram.types import InlineKeyboardButton, Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_kb():
    kb_builder=InlineKeyboardBuilder()
    buttons=[InlineKeyboardButton(text="TEST", callback_data="TEST")]
    kb_builder.row(*buttons)
    return kb_builder.as_markup()