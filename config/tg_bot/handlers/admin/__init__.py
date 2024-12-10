from tg_bot.buttons.reply import admin_btn


#admin_handlers

from tg_bot.handlers.admin.add_order import *
from tg_bot.handlers.admin.add_payment import *
from tg_bot.handlers.admin.next_payments import *
from tg_bot.handlers.admin.orders import *


@dp.message(lambda msg : msg.text == admin_secret_txt )
async def check_admin(message: Message) -> None:
    await message.answer(
        text=f"Assalomu alaykum <b><i>{message.from_user.username}</i></b> "
             f"\nadmin paneldan foydalanish uchun tugmalardan birini tanlang 👇🏿",
        parse_mode="HTML",  # Enable HTML parsing
        reply_markup=admin_btn()
    )

