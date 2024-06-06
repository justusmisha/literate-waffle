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
