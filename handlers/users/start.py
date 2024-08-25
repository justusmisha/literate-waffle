from aiogram import types

from keyboards.users.inline.form_keyboards import start_kb
from loader import dp


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(f"Добро пожаловать", reply_markup=start_kb)


@dp.callback_query_handler(lambda c: c.data == 'back_to_start')
async def cmd_start(call: types.CallbackQuery):
    await call.message.edit_text(f"Добро пожаловать", reply_markup=start_kb)
