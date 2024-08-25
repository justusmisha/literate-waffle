from html.parser import HTMLParser

from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    personal_items = State()
    transport = State()
    realty = State()
    job = State()
    services = State()
    for_home_and_garden = State()
    consumer_electronics = State()
    hobbies = State()
    animals = State()
    business = State()
    key_words = State()


class LinkParser(StatesGroup):
    url = State()


class QueryParser(StatesGroup):
    add_query = State()
    add_pages = State()
    add_city = State()


class GoogleStates(StatesGroup):
    sheet_name = State()


class SellerStates(StatesGroup):
    seller_url = State()
    page_numbers = State()