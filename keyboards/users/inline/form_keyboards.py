from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import categories


categ_buttons = [InlineKeyboardButton(text=category, callback_data=category) for category in categories]

first_kb = InlineKeyboardMarkup(row_width=2)

first_kb.add(*categ_buttons)

back_button = InlineKeyboardButton(text="Проверить другие запросы", callback_data="back")

back_kb = InlineKeyboardMarkup(row_width=1)

back_kb.add(back_button)
