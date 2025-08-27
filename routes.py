from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from forms import RegisterUser
from client import register_user, get_all_users

router = Router()


@router.message(F.text == "/start")
async def start(msg: Message, state: FSMContext):
    await state.set_state(RegisterUser.name)
    await msg.answer("Привет! Как тебя зовут?")


@router.message(RegisterUser.name)
async def get_name(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(RegisterUser.email)
    await msg.answer("Укажи, пожалуйста, свой email:")


@router.message(RegisterUser.email)
async def get_email(msg: Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    email = msg.text

    success = await register_user(name=name, email=email)

    if success:
        await msg.answer("✅ Спасибо! Ты успешно зарегистрирован.", reply_markup=ReplyKeyboardRemove())
    else:
        await msg.answer("❌ Произошла ошибка при сохранении. Попробуй позже.")

    await state.clear()

@router.message(F.text == "/users")
async def list_users(message: Message):
    users = await get_all_users()

    if not users:
        await message.answer('While we dont have users')

    text = "Users\n\n"
    for user in users:
        text += f"{user['name']} - {user['email']}\n"

    await message.answer(text)