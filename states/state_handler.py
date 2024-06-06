from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from data.config import *
from states.user_state import Form
from utils.validation import validator_for_text


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.personal_items)
async def first_cat(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    await bot.send_message(chat_id=message.chat.id,
                           text=prompt_1+message.text)
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.transport)
async def sec_cat(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text=prompt_2+message.text)
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.realty)
async def third_cat(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text=prompt_3+message.text)
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.job)
async def fourth_cat(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text=prompt_4+message.text)
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.services)
async def fifth_cat(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text=prompt_5+message.text)
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.for_home_and_garden)
async def sixth_cat(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text=prompt_6+message.text)
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.consumer_electronics)
async def seventh_cat(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text=prompt_7+message.text)
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.hobbies)
async def eighth_cat(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text=prompt_8+message.text)
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.animals)
async def nineth_cat(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text=prompt_9+message.text)
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.business)
async def tenth_cat(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text=prompt_10+message.text)
    await state.finish()
