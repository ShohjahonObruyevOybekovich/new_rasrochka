from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from asgiref.sync import sync_to_async, async_to_sync
from icecream import ic

from bot.models import User,Payment,Installment
from tg_bot.buttons.inline import phone_number_btn, months
from tg_bot.buttons.reply import menu_btn, skip
from tg_bot.buttons.text import *
from dispatcher import dp
from tg_bot.state.main import *


@dp.message(lambda msg : msg.text == add_order )
async def command_start_handler(message: Message,state : FSMContext) -> None:
    await state.set_state(Add_order.phone)
    await message.answer(text="Raqamingizni yuboring:")



@dp.message(Add_order.phone)
async def callback_handler(msg: Message,state : FSMContext) -> None:
    data = await state.get_data()
    data['phone'] = msg.text
    await state.set_data(data)
    ic(data)

    try:
        user = await sync_to_async(User.objects.filter(phone=msg.text).first)()
        ic(user)
        if user:
            await state.set_state(Add_order.product_name)
            await msg.answer("Mahsulotning nomini kiriting:")
        else:
            await state.set_state(Add_order.user_name)
            await msg.answer("To'liq ismingizni kiriting:")
    except:
        await msg.answer("Muammo kuzatildi!")

from aiogram.filters.state import StateFilter


@dp.message(StateFilter(Add_order.user_name))
async def handle_user_name(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['user_name'] = message.text
    await state.set_data(data)
    try:
        # await sync_to_async(User.objects.create)(full_name=data['user_name'],phone=data['phone_number'])
        new_customer = User.objects.create(full_name=data['user_name'],phone=data['phone'],chat_id=message.from_user.id)
        ic(new_customer)
        await state.set_state(Add_order.product_name)
        await message.answer("Mahsulotning nomini kiriting:")
    except Exception as e:
        ic(e)
        raise e from e


@dp.message(StateFilter(Add_order.product_name))  # Handle the next state
async def handle_product_name(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['product_name'] = message.text
    await state.set_data(data)
    await state.set_state(Add_order.product_price)
    await message.answer("Buyurtmaning tan narxini kiriting:")




@dp.message(Add_order.product_price)
async def product_name_handler(message: Message,state : FSMContext) -> None:
    data = await state.get_data()
    data["product_name"] = message.text
    await state.set_data(data)
    await state.set_state(Add_order.avans)
    await message.answer("Boshlang'ich to'lovni kiriting dollarda yoki skip tugmasini bosing!", reply_markup=skip())

@dp.message(Add_order.avans)
async def avans_handler(message: Message,state : FSMContext) -> None:
    data = await state.get_data()
    data['avans'] = message.text
    await state.set_data(data)
    if message.text == 'skip':
        data['avans'] ='0'
        await state.set_data(data)
    await state.set_state(Add_order.rasrochka_vaqti)
    await message.answer('Rasrochka oylarini kiriting:', reply_markup=months())

@dp.message(Add_order.rasrochka_vaqti)
async def rasrochka_muddati(message: Message,state : FSMContext) -> None:
    data = await state.get_data()
    data['rasrochka_muddati'] = message.text
    await state.set_data(data)
    ic(data)






