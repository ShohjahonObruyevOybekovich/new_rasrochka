from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from tg_bot.buttons.text import *



def menu_btn():
    k1 = KeyboardButton(text = habarnomalar_txt)
    k2 = KeyboardButton(text = orders_list_txt)
    design = [
        [k1 , k2],
    ]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)

def Login():
    keyboard1 = KeyboardButton(text = Login_txt)
    design = [[keyboard1]]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)



def admin_btn():
    keyboard1 = KeyboardButton(text = order_history_txt)
    keyboard2 = KeyboardButton(text = orders_txt)
    keyboard3 = KeyboardButton(text=add_order)
    keyboard4 = KeyboardButton(text=next_payments)
    design = [[keyboard1, keyboard2],
              [keyboard3, keyboard4],]
    return ReplyKeyboardMarkup(keyboard=design ,
                               resize_keyboard=True)


def skip():
    keyboard1 = KeyboardButton(text = "skip")
    design = [[keyboard1]]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)
