from http.client import responses

from aiogram.filters import CommandStart
from aiogram.types import Message
from asgiref.sync import sync_to_async

from bot.models import User
from tg_bot.buttons.reply import menu_btn
from tg_bot.buttons.text import *
from dispatcher import dp
from tg_bot.handlers.admin import *

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        text=f"Assalomu alaykum <b><i>{message.from_user.username}</i></b> "
             f"\nBotdan foydalanish uchun tugmalardan birini tanlang 👇🏿",
        parse_mode="HTML",  # Enable HTML parsing
        reply_markup=menu_btn()
    )

    try:
        user = await sync_to_async(User.objects.filter(chat_id=message.chat.id).first)()
        ic(user)

        # Check if the user exists
        if user:
            print("User is already registered:", user)

        else:
            print("User is not registered.")
            await sync_to_async(User.objects.create)(chat_id=message.from_user.id)

    except Exception as e:
        print(f"Error checking user registration: {e}")

@dp.message(lambda msg : msg.text == habarnomalar_txt )
async def user_notifications(msg: Message) -> None:
    user = User.objects.get(chat_id=msg.chat.id)
    print(user.objects.all())





# @dp.message(lambda msg : msg.text == Login_txt)
# async def register_handler(msg : Message , state : FSMContext):
#     await state.set_state(UserState.Student_login)
#     await msg.answer(" Student hemis loginingizni kiriting👇🏿!")
#
# @dp.message(UserState.Student_login)
# async def login(msg : Message , state : FSMContext):
#     data = await state.get_data()
#     data["Student_login"] = msg.text
#     await state.set_data(data)
#     await state.set_state(UserState.Student_password)
#     await msg.answer(text='Parolni kiriting ✏️')
#
# @dp.message(UserState.Student_password)
# async def handle_password(msg: Message, state: FSMContext):
#     # Get the data stored in state
#     user_data = await state.get_data()
#     login = user_data.get("Student_login")
#     password = msg.text
#
#     # Prepare the API request
#     url = "https://talaba.tsue.uz/rest/v1/auth/login"
#     headers = {
#         "accept": "application/json",
#         "Content-Type": "application/json",
#     }
#     payload = {
#         "login": login,
#         "password": password
#     }
#
#     # Send the request to the API
#     try:
#         response = requests.post(url, json=payload, headers=headers)
#         response_data = response.json()
#
#         if response.status_code == 200 and response_data.get("success"):
#             token = response_data["data"]["token"]
#             query = update(User).values(login_code = login,password=password, token = token).where(User.chat_id == msg.from_user.id)
#             session.execute(query)
#             session.commit()
#             await msg.answer(f"✅ Muvaffaqiyatli login qilindi!\n", reply_markup=menu_btn())
#         else:
#             error_message = response_data.get("error", "Noma'lum xato yuz berdi.")
#             print(error_message)
#             await msg.answer(f"❌ Xatolik yuz berdi 1",reply_markup=Login())
#
#     except Exception as e:
#         print(e)
#         await msg.answer(f"❌ Xatolik yuz berdi",reply_markup=Login())
#
#     # Reset the state after processing
#     await state.clear()


