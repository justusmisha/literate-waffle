from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from states.user_state import Form
from utils.functions import prompt_maker_en, google_prompts
from utils.neuro_models.meta import meta_ai
from utils.translator import deep_translator
from utils.validation import validator_for_text


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.personal_items)
async def first_cat(message: types.Message, state: FSMContext):
    # text = prompt_maker_en(deep_translator(message.text.split()[0], 'ru', 'en'),
    #                        deep_translator("Личные вещи", 'ru', 'en'), deep_translator(message.text, 'ru', 'en'))
    prompt_pattern = deep_translator(google_prompts("Личные вещи"), "ru", "en") + 'on the topic ' + deep_translator(message.text, 'ru', 'en')
    await bot.send_message(chat_id=message.chat.id,
                           text=meta_ai(prompt_pattern))
    await state.finish()


# @dp.message_handler(lambda message: validator_for_text(message.text), state=Form.transport)
# async def sec_cat(message: types.Message, state: FSMContext):
#     text = prompt_maker_en(deep_translator(message.text.split()[0], 'ru', 'en'), deep_translator("Транспорт", 'ru','en'), deep_translator(message.text,'ru', 'en'))
#     await bot.send_message(chat_id=message.chat.id,
#                            text=meta_ai(text))
#     await state.finish()


# @dp.message_handler(lambda message: validator_for_text(message.text), state=Form.realty)
# async def third_cat(message: types.Message, state: FSMContext):
#     text = prompt_maker_en(deep_translator(message.text.split()[0], 'ru', 'en'), deep_translator("Недвижимость", 'ru','en'), deep_translator(message.text,'ru', 'en'))
#     await bot.send_message(chat_id=message.chat.id,
#                            text=meta_ai(text))
#     await state.finish()


# @dp.message_handler(lambda message: validator_for_text(message.text), state=Form.job)
# async def fourth_cat(message: types.Message, state: FSMContext):
#     text = prompt_maker_en(deep_translator(message.text.split()[0], 'ru', 'en'), deep_translator("Работа", 'ru','en'), deep_translator(message.text,'ru', 'en'))
#     await bot.send_message(chat_id=message.chat.id,
#                            text=meta_ai(text))
#     await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.services)
async def fifth_cat(message: types.Message, state: FSMContext):
    phrase_to_replace = "<ключевые слова от пользователя>"

    updated_prompt = google_prompts("Услуги").replace(phrase_to_replace, message.text)
    prompt_pattern = deep_translator(updated_prompt, 'ru', 'en')
    await bot.send_message(chat_id=message.chat.id,
                           text=meta_ai(prompt_pattern))
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.for_home_and_garden)
async def sixth_cat(message: types.Message, state: FSMContext):
    text = prompt_maker_en(deep_translator(message.text.split()[0], 'ru', 'en'),
                           deep_translator("Для дома и дачи", 'ru', 'en'), deep_translator(message.text, 'ru', 'en'))
    prompt_pattern = text + "Also mention these instructions " + deep_translator(google_prompts("Для дома и дачи"),
                                                                                 'ru',
                                                                                 'en')
    await bot.send_message(chat_id=message.chat.id,
                           text=meta_ai(prompt_pattern))
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.consumer_electronics)
async def seventh_cat(message: types.Message, state: FSMContext):
    text = prompt_maker_en(deep_translator(message.text.split()[0], 'ru', 'en'),
                           deep_translator("Бытовая электроника", 'ru', 'en'),
                           deep_translator(message.text, 'ru', 'en'))
    prompt_pattern = text + "Also mention these instructions " + deep_translator(google_prompts("Бытовая электроника"),
                                                                                 'ru',
                                                                                 'en')
    await bot.send_message(chat_id=message.chat.id,
                           text=meta_ai(prompt_pattern))
    await state.finish()

# @dp.message_handler(lambda message: validator_for_text(message.text), state=Form.hobbies)
# async def eighth_cat(message: types.Message, state: FSMContext):
#     text = prompt_maker_en(deep_translator(message.text.split()[0], 'ru', 'en'), deep_translator("Хобби и отдых", 'ru','en'), deep_translator(message.text,'ru', 'en'))
#     await bot.send_message(chat_id=message.chat.id,
#                            text=meta_ai(text))
#     await state.finish()
#
#
# @dp.message_handler(lambda message: validator_for_text(message.text), state=Form.animals)
# async def nineth_cat(message: types.Message, state: FSMContext):
#     text = prompt_maker_en(deep_translator(message.text.split()[0], 'ru', 'en'), deep_translator("Животные", 'ru','en'), deep_translator(message.text,'ru', 'en'))
#     await bot.send_message(chat_id=message.chat.id,
#                            text=meta_ai(text))
#     await state.finish()
#
#
# @dp.message_handler(lambda message: validator_for_text(message.text), state=Form.business)
# async def tenth_cat(message: types.Message, state: FSMContext):
#     text = prompt_maker_en(deep_translator(message.text.split()[0], 'ru', 'en'), deep_translator("Для бизнеса", 'ru','en'), deep_translator(message.text,'ru', 'en'))
#     await bot.send_message(chat_id=message.chat.id,
#                            text=meta_ai(text))
#     await state.finish()
