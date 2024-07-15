from aiogram.types import CallbackQuery

from keyboards.users.inline import first_kb
from loader import dp, bot
from states.user_state import Form


@dp.callback_query_handler(lambda query: query.data == 'Личные вещи', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.personal_items.set()


@dp.callback_query_handler(lambda query: query.data == 'Транспорт', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.transport.set()


@dp.callback_query_handler(lambda query: query.data == 'Недвижимость', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.realty.set()


@dp.callback_query_handler(lambda query: query.data == 'Работа', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.job.set()


@dp.callback_query_handler(lambda query: query.data == 'Услуги', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.services.set()


@dp.callback_query_handler(lambda query: query.data == 'Для дома и дачи', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.for_home_and_garden.set()


@dp.callback_query_handler(lambda query: query.data == 'Бытовая электроника', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.consumer_electronics.set()


@dp.callback_query_handler(lambda query: query.data == 'Хобби и отдых', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.hobbies.set()


@dp.callback_query_handler(lambda query: query.data == 'Животные', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.animals.set()


@dp.callback_query_handler(lambda query: query.data == 'Для бизнеса', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.business.set()


@dp.callback_query_handler(lambda query: query.data == 'Генератор ключевых слов', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите товар или услугу чтобы сгенерировать ключевые слова.")

    await Form.key_words.set()


@dp.callback_query_handler(lambda query: query.data == 'back', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await callback_query.message.answer(f"Выберите категорию", reply_markup=first_kb)

