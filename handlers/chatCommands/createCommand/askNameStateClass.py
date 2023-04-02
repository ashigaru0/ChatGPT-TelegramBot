from aiogram.fsm.state import StatesGroup, State


class createChatState(StatesGroup):
    choiceName = State()
