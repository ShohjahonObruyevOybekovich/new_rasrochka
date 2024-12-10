from aiogram.fsm.state import StatesGroup, State


class Add_order(StatesGroup):
    phone = State()
    user_name = State()
    product_name = State()
    product_price = State()
    avans = State()
    rasrochka_vaqti = State()
