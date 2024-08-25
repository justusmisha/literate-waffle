from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import keywords
from keyboards.users.inline.form_keyboards import back_kb, categories_kb, start_kb
from loader import dp, bot
from states.user_state import Form
from utils.functions import google_prompts, text_formating, text_checker
from utils.neuro_models.yandexGPT import yandexGPT
from utils.validation import validator_for_text


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.personal_items)
async def first_cat(message: types.Message, state: FSMContext):
    if message.text != '/start':

        updated_prompt = google_prompts("Личные вещи").replace(keywords, message.text)
        text = await yandexGPT("Напиши хороший текст следуя структуре и инструкциям. Он должен быть полноценным и не "
                               "нуждаться в редакции. Исключи слова 'Заголовок', 'Начало текста', 'Призыв к действию' и "
                               "подобные технические фразы."
                               + updated_prompt + "Напиши минимум 250 слов.")
        await bot.send_message(chat_id=message.chat.id,
                               text=text_formating(text),
                               reply_markup=back_kb)
        await state.finish()
    else:
        await message.answer(f"Добро пожаловать", reply_markup=start_kb)

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
    if message.text != '/start':
        updated_prompt = google_prompts("Услуги").replace(keywords, message.text)
        updated_prompt = text_checker(updated_prompt)
        text = await yandexGPT("Напиши хороший текст следуя структуре и инструкциям. Он должен быть полноценным и не "
                               "нуждаться в редакции. Исключи слова 'Заголовок', 'Начало текста', 'Призыв к действию' и "
                               "подобные технические фразы. Выдели каждый призыв к действию пробелами"
                               + updated_prompt)
        await bot.send_message(chat_id=message.chat.id,
                               text=text_formating(text),
                               reply_markup=back_kb)
        await state.finish()
    else:
        await message.answer(f"Добро пожаловать", reply_markup=start_kb)


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.for_home_and_garden)
async def sixth_cat(message: types.Message, state: FSMContext):
    if message.text != '/start':

        updated_prompt = google_prompts("Для дома и дачи").replace(keywords, message.text)
        text = await yandexGPT("Напиши хороший текст следуя структуре и инструкциям. Он должен быть полноценным и не "
                               "нуждаться в редакции. Исключи слова 'Заголовок', 'Начало текста', 'Призыв к действию' и "
                               "подобные технические фразы."
                               + updated_prompt + "Напиши минимум 250 слов.")
        await bot.send_message(chat_id=message.chat.id,
                               text=text_formating(text),
                               reply_markup=back_kb)
        await state.finish()
    else:
        await message.answer(f"Добро пожаловать", reply_markup=start_kb)


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.consumer_electronics)
async def seventh_cat(message: types.Message, state: FSMContext):
    if message.text != '/start':
        updated_prompt = google_prompts("Бытовая электроника").replace(keywords, message.text)
        text = await yandexGPT("Напиши хороший текст следуя структуре и инструкциям. Он должен быть полноценным и не "
                               "нуждаться в редакции. Исключи слова 'Заголовок', 'Начало текста', 'Призыв к действию' и "
                               "подобные технические фразы."
                               + updated_prompt + "Напиши минимум 250 слов.")
        await bot.send_message(chat_id=message.chat.id,
                               text=text_formating(text),
                               reply_markup=back_kb)
        await state.finish()
    else:
        await message.answer(f"Добро пожаловать", reply_markup=start_kb)


@dp.message_handler(lambda message: validator_for_text(message.text), state=Form.key_words)
async def key_words_cat(message: types.Message, state: FSMContext):
    if message.text != '/start':
        prompt = """Ты специалист по СЕО и собираешь ключевые запросы для сайта объявлений Авито.
         Я предлагаю тебе название товара или услуги, а ты выдаешь ключевые продающие фразы списком из 10 штук.
          Постарайся подобрать фразы разного формата чтоб избежать повторов. <ключевые слова от пользователя>"""
        updated_prompt = prompt.replace(keywords, message.text)
        text = await yandexGPT(updated_prompt)
        await bot.send_message(chat_id=message.chat.id,
                               text=text_formating(text),
                               reply_markup=back_kb)
        await state.finish()
    else:
        await message.answer(f"Добро пожаловать", reply_markup=start_kb)
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
