from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import categories


categ_buttons = [InlineKeyboardButton(text=category, callback_data=category) for category in categories]

first_kb = InlineKeyboardMarkup()

first_kb.add(*categ_buttons)
