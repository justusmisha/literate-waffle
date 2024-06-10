import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.user_state import Form
from utils.validation import validate_name_surname, validate_phone, validate_instagram


# @dp.message_handler(state=Form.name_surname, content_types=types.ContentType.TEXT)
# async def process_name(message: types.Message, state: FSMContext):
#     if not validate_name_surname(message.text):
#         await message.answer("❗️ Данные введены неверно. Введите имя и фамилию через пробел.")
#         return
#
#     async with state.proxy() as data:
#         data['name_surname'] = message.text
#     await Form.next()
#     await message.answer(f"▪️Номер телефона (без +)\n"
#                         f"Пример: 89101282705")
#
#
# @dp.message_handler(state=Form.phone, content_types=types.ContentType.TEXT)
# async def process_phone(message: types.Message, state: FSMContext):
#     if not validate_phone(message.text):
#         await message.answer("❗️ Номер телефона введен неверно. Попробуйте еще раз.")
#         return
#
#     async with state.proxy() as data:
#         data['phone'] = message.text
#     await Form.next()
#     await message.answer("▪️Ссылка на Inst:\n*аккаунт должен быть открыт*")
#
#
# @dp.callback_query_handler(text='reset', state=Form.instagram)
# async def process_reset(call: types.CallbackQuery, state: FSMContext):
#     await call.message.answer("❌ Ввод данных сброшен. Начните заново командой /start.")
#     await state.finish()
