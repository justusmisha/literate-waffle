import json
import urllib.parse

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from api.endpooints import UserEndpoints
from data import config
from keyboards.users.inline.form_keyboards import market_analyze_kb, categories_kb, google_sheets_kb, after_parser_kb, \
    query_kb, query_execute_kb, start_kb, google_sheet_menu_kb, all_google_sheets_kb, seller_kb, sellers_kb
from loader import dp, bot, api_client
from states.user_state import Form, LinkParser, QueryParser, GoogleStates, SellerStates


@dp.callback_query_handler(lambda c: c.data == '🤖 Генерация')
async def generator_kb(call: CallbackQuery):
    await call.message.edit_text(text='Выберете категорию', reply_markup=categories_kb)


@dp.callback_query_handler(lambda query: query.data == '👕 Личные вещи', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.personal_items.set()


@dp.callback_query_handler(lambda query: query.data == '🗣 Услуги', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.services.set()


@dp.callback_query_handler(lambda query: query.data == '🏡 Для дома и дачи', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.for_home_and_garden.set()


@dp.callback_query_handler(lambda query: query.data == '🛠 Бытовая электроника', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите ключевые слова для товара или услуги из категории «{callback_query.data}»")

    await Form.consumer_electronics.set()


@dp.callback_query_handler(lambda query: query.data == '🔑 Генератор ключевых слов', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           text=f"Введите товар или услугу чтобы сгенерировать ключевые слова.")

    await Form.key_words.set()


@dp.callback_query_handler(lambda query: query.data == 'back', state='*')
async def cmd_start(callback_query: CallbackQuery):
    await callback_query.message.answer(f"Выберите категорию", reply_markup=categories_kb)


@dp.callback_query_handler(lambda c: c.data == '📊 Анализ рыночной ситуации', state='*')
async def market_analyze(callback_query: CallbackQuery):
    kb = await market_analyze_kb()
    await callback_query.message.edit_text(text='Анализ рычночной ситуации', reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data == 'avito_parser_butt')
async def avito_parser(call: CallbackQuery):
    await call.message.edit_text('Введите запрос для поиска', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='📊 Анализ рыночной ситуации')))


@dp.callback_query_handler(lambda c: c.data == 'link_menu')
async def link_menu(call: CallbackQuery):
    await call.message.edit_text(text='Чтобы cпарсить ссылку введите url', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='📊 Анализ рыночной ситуации')))
    await LinkParser.url.set()


@dp.message_handler(state=LinkParser.url)
async def link_menu_google(message: Message, state: FSMContext):
    if message.text != '/start':
        await state.update_data(url=message.text)
        kb = await google_sheets_kb()
        if isinstance(kb, str):
            await message.answer(text=kb, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='📊 Анализ рыночной ситуации')))
        else:
            await message.answer('URL добавлен, теперь выберете Google Sheet в который будет спаршена ссылка', reply_markup=kb)
    else:
        await message.answer(f"Добро пожаловать", reply_markup=start_kb)
        await state.finish()


@dp.callback_query_handler(lambda c: c.data.startswith('exact_sheet_'), state='*')
async def link_menu_google(call: CallbackQuery, state: FSMContext):
    google_sheet_name = str(call.data.split('exact_sheet_')[-1])
    await state.update_data(google_sheet_name=google_sheet_name)
    data = await state.get_data()
    waiting_message = await call.message.answer(config.PARSING_MESSAGE)
    sheet = await api_client.post(UserEndpoints.google_sheet_by_name, json={'sheet_name': google_sheet_name})
    if sheet:
        kb = await after_parser_kb(sheet['sheets']['sheet_id'])
    result = await api_client.post(UserEndpoints.parse_one_link, json=data)
    await state.finish()

    if result:
        await waiting_message.delete()
        await call.message.edit_text(text=f'✅ Запрос закончен заняв {result["time"]} секунд.', reply_markup=kb)
    else:
        await waiting_message.delete()
        await call.message.answer(text='❌ Возникла ошибка при парсинге одной ссылки')


@dp.callback_query_handler(lambda c: c.data == 'query_menu')
async def query_menu(call: CallbackQuery):
    kb = await query_kb()
    await call.message.edit_text(text='Работа с запросами', reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data == 'query_add', state='*')
async def query_add_menu(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text='Введите запрос который хотите добавить')
    await QueryParser.add_query.set()


@dp.message_handler(state=QueryParser.add_query)
async def query_add_handler(message: Message, state: FSMContext):
    if message.text != '/start':
        query = str(message.text)
        await state.update_data(query=query)
        await message.answer(text='Введите количество страниц для парсинга')
        await QueryParser.add_pages.set()
    else:
        await message.answer(f"Добро пожаловать", reply_markup=start_kb)
        await state.finish()


@dp.message_handler(state=QueryParser.add_pages)
async def query_add_handler(message: Message, state: FSMContext):
    if message.text != '/start':
        page_numbers = str(message.text)
        await state.update_data(page_numbers=page_numbers)
        await message.answer(text='Введите город')
        await QueryParser.add_city.set()
    else:
        await message.answer(f"Добро пожаловать", reply_markup=start_kb)
        await state.finish()


@dp.message_handler(state=QueryParser.add_city)
async def query_add_handler(message: Message, state: FSMContext):
    city = str(message.text)
    await state.update_data(city=city)
    data = await state.get_data()
    waiting_message = await message.answer(config.PARSING_MESSAGE)
    result = await api_client.post(UserEndpoints.save_by_query, json=data)
    try:
        if result:
            await message.answer(text='✅ Запрос добавлен\n'
                                      f'Заняло {result["time"]} секунд',
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='query_menu')))
        else:
            await message.answer(text='❌ Возникла ошибка при добавлении запроса',
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='query_menu')))
    except Exception as e:
        await waiting_message.delete()
    finally:
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'query_execute', state='*')
async def query_execute_menu(call: CallbackQuery, state: FSMContext):
    queries = await api_client.get(UserEndpoints.all_queries)
    if queries:
        kb = await query_execute_kb(queries['queries'])
        await call.message.edit_text(text='Выберите запрос для парсинга', reply_markup=kb)
    else:
        await call.message.answer(text='❌ Возникла ошибка при поиске запросов')


@dp.callback_query_handler(lambda c: c.data.startswith('query_execute_'), state='*')
async def query_execute_handler(call: CallbackQuery, state: FSMContext):
    query = str(call.data.split('query_execute_')[-1])
    await state.update_data(query=query)
    kb = await google_sheets_kb('exec')
    if isinstance(kb, str):
        await call.message.answer(text=kb)
    else:
        await call.message.edit_text(text=f'Выберите Google Doc в который будем парсить запрос "{query}"',
                                     reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data.startswith('exec_exact_sheet_'), state='*')
async def qery_execute_google(call: CallbackQuery, state: FSMContext):
    google_sheet = str(call.data.split('exec_exact_sheet_')[-1])
    data = await state.get_data()
    waiting_message = await call.message.answer(config.PARSING_MESSAGE)
    json = {'google_sheet_name': google_sheet,
            'query': data['query']}
    result = await api_client.post(UserEndpoints.link_executor, json=json)
    sheet = await api_client.post(UserEndpoints.google_sheet_by_name, json={'sheet_name': google_sheet})
    if result:
        kb = await after_parser_kb(sheet['sheets']['sheet_id'])
        await call.message.edit_text(text='✅ Данные добавлены в Google Doc', reply_markup=kb)
        await waiting_message.delete()
    else:
        await call.message.answer(text='❌ Возникла ошибка при парсинге в Google Doc', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='back_to_start')))


@dp.callback_query_handler(lambda c: c.data == 'query_delete', state='*')
async def query_delete_menu(call: CallbackQuery, state: FSMContext):
    queries = await api_client.get(UserEndpoints.all_queries)
    if queries:
        kb = await query_execute_kb(queries['queries'], 'delete')
        await call.message.edit_text(text='Выберите запрос для удаления', reply_markup=kb)
    else:
        await call.message.answer(text='❌ Возникла ошибка при поиске запросов')


@dp.callback_query_handler(lambda c: c.data.startswith('delete_query_'), state='*')
async def query_delete_menu(call: CallbackQuery, state: FSMContext):
    query = str(call.data.split('delete_query_')[-1])
    result = await api_client.delete(UserEndpoints.delete_query, json={'query_name': query})
    if result:
        await call.message.edit_text(text='✅ Запрос удален!', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='query_menu')))
    else:
        await call.message.answer(text='❌ Возникла ошибка с удалением запроса', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='query_menu')))


@dp.callback_query_handler(lambda c: c.data == 'google_sheet_menu', state='*')
async def google_sheet_menu(call: CallbackQuery, state: FSMContext):
    kb = await google_sheet_menu_kb()
    await call.message.edit_text(text='Детальный просмотр рздела Google Doc', reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data == 'add_google_sheet', state='*')
async def add_google_sheet(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text='Введите название документа')
    await GoogleStates.sheet_name.set()


@dp.message_handler(state=GoogleStates.sheet_name)
async def sheet_name_handler(message: Message, state: FSMContext):
    sheet_name = message.text
    await state.finish()
    result = await api_client.post(UserEndpoints.create_sheet, json={'sheet_name': sheet_name})
    if result:
        await message.answer(text='✅ Google Doc создан', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='google_sheet_menu')))
    else:
        await message.answer(text='❌ Произошла ошибка при создании Google Doc')


@dp.callback_query_handler(lambda c: c.data == 'all_google_sheet', state='*')
async def add_google_sheet(call: CallbackQuery, state: FSMContext):
    result = await api_client.get(UserEndpoints.all_google_sheets)
    kb = await all_google_sheets_kb(result['sheets'])
    await call.message.edit_text(text='Все Google документы', reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data == 'seller_menu', state='*')
async def seller_menu(call: CallbackQuery, state: FSMContext):
    kb = await seller_kb()
    await call.message.edit_text(text='Работа с продавцами', reply_markup=kb)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'seller_add', state='*')
async def seller_add_menu(call: CallbackQuery, state: FSMContext):
    await SellerStates.seller_url.set()
    await call.message.edit_text(text='Введите ссылку на продавца', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='seller_menu')))


@dp.message_handler(state=SellerStates.seller_url)
async def seller_add_handler(message: Message, state: FSMContext):
    await state.finish()
    url = str(message.text)
    waiting_message = await message.answer(config.PARSING_MESSAGE)
    result = await api_client.post(UserEndpoints.add_seller, json={'url': url})
    if result:
        await message.answer(text=f'✅ Продавец {result["seller_name"]} добавлен успешно', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='seller_menu')))
        await waiting_message.delete()
    else:
        await message.answer(text='❌ Произошла ошибка при доабвлении продавца', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='seller_menu')))
        await waiting_message.delete()


@dp.callback_query_handler(lambda c: c.data == 'seller_execute', state='*')
async def seller_execute_menu(call: CallbackQuery, state: FSMContext):
    await state.finish()
    kb = await sellers_kb('execute')
    await call.message.edit_text(text='Выберите продавца', reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data.startswith('execute_seller_'), state='*')
async def seller_exec_habdlers(call: CallbackQuery, state: FSMContext):
    seller_name = str(call.data.split('execute_seller_')[-1])
    await state.update_data(seller_name=seller_name)
    kb = await google_sheets_kb('seller')
    await call.message.edit_text('Выберите Google Doc для парсинга', reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data.startswith('seller_exact_sheet_'), state='*')
async def seller_doc_handler(call: CallbackQuery, state: FSMContext):
    google_sheet = str(call.data.split('seller_exact_sheet_')[-1])
    await state.update_data(google_sheet=google_sheet)
    await call.message.edit_text(text='Введите количество страниц для парсинга', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='seller_menu')))
    await SellerStates.page_numbers.set()


@dp.message_handler(state=SellerStates.page_numbers)
async def seller_ages_handler(message: Message, state: FSMContext):
    page_numbers = int(message.text)
    await state.update_data(page_numbers=page_numbers)
    data = await state.get_data()
    await state.finish()
    waiting_message = await message.answer(config.PARSING_MESSAGE)
    result = await api_client.post(UserEndpoints.parse_seller, json=data)

    if not result:
        await message.answer(text='❌ Произошла ошибка при парсинге продавца', reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(text='◀️ Назад', callback_data='seller_menu')))
        await waiting_message.delete()
    else:
        await message.answer(text='✅ Продавец спаршен успешно', reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(text='◀️ Назад', callback_data='seller_menu')))
        await waiting_message.delete()


@dp.callback_query_handler(lambda c: c.data == 'seller_delete', state='*')
async def seller_delete(call: CallbackQuery, state: FSMContext):
    kb = await sellers_kb('delete')
    await call.message.edit_text(text='Выберите продавца которого хотите удалить', reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data.startswith('delete_seller_'), state='*')
async def seller_exec_habdlers(call: CallbackQuery, state: FSMContext):
    seller_name = str(call.data.split('delete_seller_')[-1])
    result = await api_client.delete(UserEndpoints.delete_seller, json={'seller_name': seller_name})
    if result:
        await call.message.edit_text(text='✅ Продавец удален', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='seller_menu')))
    else:
        await call.message.answer(text='❌ Возникла ошибка с удалением продавца', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️ Назад', callback_data='seller_menu')))
