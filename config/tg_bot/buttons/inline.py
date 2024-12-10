from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


def phone_number_btn():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = "contact", request_contact=True) ]] , resize_keyboard=True)

def months():
    uch_oy = InlineKeyboardButton(text='3 oylik',
                                    callback_data="3 oylik")
    olti_oy = InlineKeyboardButton(text='6 oylik',callback_data="6 oylik")
    toqqiz_oy  = InlineKeyboardButton(text='12 oylik',callback_data="12 oylik")
    yigirma_turt = InlineKeyboardButton(text='24 oylik',callback_data="24 oylik")

    return InlineKeyboardMarkup(inline_keyboard=[[uch_oy, olti_oy],[toqqiz_oy, yigirma_turt]] )


