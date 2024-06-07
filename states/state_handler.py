from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from data.config import *
from states.user_state import Form
from utils.functions import prompt_maker, prompt_maker_en
from utils.neuro_models.hermes import hermes
from utils.neuro_models.meta import meta_ai
from utils.neuro_models.mistral_ai import mistralai
from utils.translator import translator
from utils.validation import validator_for_text


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.personal_items)
async def first_cat(message: types.Message, state: FSMContext):
    text = prompt_maker_en(translator(message.text.split()[0] + " " + message.text.split()[1], 'en'), translator("Личные вещи", 'en'), translator(message.text, 'en'))
    print(meta_ai(text))
    await bot.send_message(chat_id=message.chat.id,
                           text=meta_ai(text))
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.transport)
async def sec_cat(message: types.Message, state: FSMContext):
    text = prompt_maker(prompt_common, "Транспорт", message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=hermes(translator(text, 'en')))
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.realty)
async def third_cat(message: types.Message, state: FSMContext):
    text = prompt_maker(prompt_common, "Недвижимость", message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=hermes(translator(text, 'en')))
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.job)
async def fourth_cat(message: types.Message, state: FSMContext):
    text = prompt_maker(prompt_common, "Работа", message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=hermes(translator(text, 'en')))
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.services)
async def fifth_cat(message: types.Message, state: FSMContext):
    text = prompt_maker(prompt_common, "Услуги", message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=hermes(translator(text, 'en')))
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.for_home_and_garden)
async def sixth_cat(message: types.Message, state: FSMContext):
    text = prompt_maker(prompt_common, "Для дома и дачи", message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=hermes(translator(text, 'en')))
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.consumer_electronics)
async def seventh_cat(message: types.Message, state: FSMContext):
    text = prompt_maker(prompt_common, "Бытовая электроника", message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=hermes(translator(text, 'en')))
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.hobbies)
async def eighth_cat(message: types.Message, state: FSMContext):
    text = prompt_maker(prompt_common, "Хобби и отдых", message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=hermes(translator(text, 'en')))
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.animals)
async def nineth_cat(message: types.Message, state: FSMContext):
    text = prompt_maker(prompt_common, "Животные", message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=hermes(translator(text, 'en')))
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.business)
async def tenth_cat(message: types.Message, state: FSMContext):
    text = prompt_maker(prompt_common, "Для бизнеса", message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=hermes(translator(text, 'en')))
    await state.finish()
