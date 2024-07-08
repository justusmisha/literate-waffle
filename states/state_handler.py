from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from states.user_state import Form
from utils.functions import prompt_maker_en, google_prompts, text_formating
from utils.neuro_models.meta import meta_ai
from utils.neuro_models.yandexGPT import yandexGPT
from utils.translator import deep_translator
from utils.validation import validator_for_text


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.personal_items)
async def first_cat(message: types.Message, state: FSMContext):
    phrase_to_replace = "<ключевые слова от пользователя>"

    updated_prompt = google_prompts("Личные вещи").replace(phrase_to_replace, message.text)
    text = await yandexGPT("Напиши хороший текст следуя структуре и инструкциям. Он должен быть полноценным и не "
                           "нуждаться в редакции. Исключи слова 'Заголовок', 'Начало текста', 'Призыв к действию' и "
                           "подобные технические фразы."
                           + updated_prompt + "Напиши минимум 250 слов.")
    await bot.send_message(chat_id=message.chat.id,
                           text=text_formating(text))


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
    # prompt_pattern = deep_translator(updated_prompt, 'ru', 'en')
    text = await yandexGPT("Напиши хороший текст следуя структуре и инструкциям. Он должен быть полноценным и не "
                           "нуждаться в редакции. Исключи слова 'Заголовок', 'Начало текста', 'Призыв к действию' и "
                           "подобные технические фразы. Выдели каждый призыв к действию пробелами"
                           + updated_prompt + "Напиши минимум 200 слов и используй эмодзи.")
    await bot.send_message(chat_id=message.chat.id,
                           text=text_formating(text))
    await state.finish()


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.for_home_and_garden)
async def sixth_cat(message: types.Message, state: FSMContext):
    phrase_to_replace = "<ключевые слова от пользователя>"

    updated_prompt = google_prompts("Для дома и дачи").replace(phrase_to_replace, message.text)
    text = await yandexGPT("Напиши хороший текст следуя структуре и инструкциям. Он должен быть полноценным и не "
                           "нуждаться в редакции. Исключи слова 'Заголовок', 'Начало текста', 'Призыв к действию' и "
                           "подобные технические фразы."
                           + updated_prompt + "Напиши минимум 250 слов.")
    await bot.send_message(chat_id=message.chat.id,
                           text=text_formating(text))


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.consumer_electronics)
async def seventh_cat(message: types.Message, state: FSMContext):
    phrase_to_replace = "<ключевые слова от пользователя>"

    updated_prompt = google_prompts("Бытовая электроника").replace(phrase_to_replace, message.text)
    text = await yandexGPT("Напиши хороший текст следуя структуре и инструкциям. Он должен быть полноценным и не "
                           "нуждаться в редакции. Исключи слова 'Заголовок', 'Начало текста', 'Призыв к действию' и "
                           "подобные технические фразы."
                           + updated_prompt + "Напиши минимум 250 слов.")
    await bot.send_message(chat_id=message.chat.id,
                           text=text_formating(text))

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
