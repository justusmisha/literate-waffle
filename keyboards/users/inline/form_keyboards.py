from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from api.endpooints import UserEndpoints
from data.config import categories, start_buttons_list
from loader import api_client

start_buttons = [InlineKeyboardButton(text=button, callback_data=button) for button in start_buttons_list]
start_kb = InlineKeyboardMarkup(row_width=1)
start_kb.add(*start_buttons)

categ_buttons = [InlineKeyboardButton(text=category, callback_data=category) if category != '◀️ Назад' else InlineKeyboardButton(text=category, callback_data='back_to_start') for category in categories]
categories_kb = InlineKeyboardMarkup(row_width=2)
categories_kb.add(*categ_buttons)

back_button = InlineKeyboardButton(text="◀️ Назад", callback_data="back")
back_kb = InlineKeyboardMarkup(row_width=1)
back_kb.add(back_button)


async def market_analyze_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text='🔗 Ссылка', callback_data='link_menu')
    b2 = InlineKeyboardButton(text='🗣️ Запрос', callback_data='query_menu')
    b3 = InlineKeyboardButton(text='💸 Продавец', callback_data='seller_menu')
    b4 = InlineKeyboardButton(text='📄 Гугл документы', callback_data='google_sheet_menu')
    b5 = InlineKeyboardButton(text='◀️ Назад', callback_data='back_to_start')
    kb.add(b1, b2, b3, b4, b5)
    return kb


async def query_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton(text='🔎 Добавить поисковой запрос', callback_data='query_add')
    b2 = InlineKeyboardButton(text='Парсинг по запросу', callback_data='query_execute')
    b3 = InlineKeyboardButton(text='Удалить запрос', callback_data='query_delete')
    b4 = InlineKeyboardButton(text='◀️ Назад', callback_data='📊 Анализ рыночной ситуации')
    kb.add(b1, b2, b3, b4)
    return kb


async def google_sheets_kb(*args) -> InlineKeyboardMarkup or str:
    kb = InlineKeyboardMarkup(row_width=1)
    response = await api_client.get(UserEndpoints.all_google_sheets)
    callback_data = 'back_to_start'
    if response['status']:
        for sheet in response['sheets']:
            if args and args[0] == 'exec':
                kb.add(InlineKeyboardButton(text=sheet['sheet_name'], callback_data=f'exec_exact_sheet_{sheet["sheet_name"]}'))
                callback_data = 'query_menu'
            elif args and args[0] == 'seller':
                kb.add(InlineKeyboardButton(text=sheet['sheet_name'],
                                            callback_data=f'seller_exact_sheet_{sheet["sheet_name"]}'))
                callback_data = 'seller_menu'
            else:
                kb.add(InlineKeyboardButton(text=sheet['sheet_name'], callback_data=f'exact_sheet_{sheet["sheet_name"]}'))
        back_button = InlineKeyboardButton(text='◀️ Назад', callback_data=callback_data)
        kb.add(back_button)
        return kb
    else:
        return 'Возникла проблема с загрузкой Google Sheets'


async def after_parser_kb(sheet_id) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    sheet_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}'
    kb.add(InlineKeyboardButton(text="Google Документ", url=sheet_url))
    kb.add(InlineKeyboardButton(text='◀️ Назад', callback_data='back_to_start'))
    return kb


async def query_execute_kb(queries, *args) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    for query in queries:
        if args and args[0] == 'delete':
            kb.add(InlineKeyboardButton(text=query['query'], callback_data=f'delete_query_{query["query"]}'))
        else:
            kb.add(InlineKeyboardButton(text=query['query'], callback_data=f'query_execute_{query["query"]}'))
    kb.add(InlineKeyboardButton(text='◀️ Назад', callback_data='query_menu'))
    return kb


async def google_sheet_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton(text='Добавить Google Doc', callback_data=f'add_google_sheet'))
    kb.add(InlineKeyboardButton(text='Все Google Docs', callback_data=f'all_google_sheet'))
    kb.add(InlineKeyboardButton(text='◀️ Назад', callback_data='📊 Анализ рыночной ситуации'))
    return kb


async def all_google_sheets_kb(sheets: list) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    for sheet in sheets:
        sheet_url = f'https://docs.google.com/spreadsheets/d/{sheet["sheet_id"]}'
        kb.add(InlineKeyboardButton(text=sheet['sheet_name'], url=sheet_url))
    kb.add(InlineKeyboardButton(text='◀️ Назад', callback_data='google_sheet_menu'))
    return kb


async def seller_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton(text='🔎 Добавить продавца', callback_data='seller_add')
    b2 = InlineKeyboardButton(text='Парсинг по продавцу', callback_data='seller_execute')
    b3 = InlineKeyboardButton(text='Удалить продавца', callback_data='seller_delete')
    b4 = InlineKeyboardButton(text='◀️ Назад', callback_data='📊 Анализ рыночной ситуации')
    kb.add(b1, b2, b3, b4)
    return kb


async def sellers_kb(*args) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    sellers = await api_client.get(UserEndpoints.all_sellers)
    for seller in sellers['sellers']:
        if args and args[0] == 'delete':
            kb.add(InlineKeyboardButton(text=seller['seller_name'],
                                        callback_data=f'delete_seller_{seller["seller_name"]}'))
        else:
            kb.add(InlineKeyboardButton(text=seller['seller_name'], callback_data=f'execute_seller_{seller["seller_name"]}'))
    kb.add(InlineKeyboardButton(text='Назад', callback_data='seller_execute'))
    return kb