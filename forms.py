from aiogram.fsm.state import StatesGroup, State

class RegisterUser(StatesGroup):
    name = State()
    email = State()