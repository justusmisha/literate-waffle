from aiogram import types

from keyboards.users.inline import first_kb
from loader import dp


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(f"Выберите категорию", reply_markup=first_kb)



