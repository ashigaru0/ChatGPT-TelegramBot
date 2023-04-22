from aiogram.fsm.state import StatesGroup, State


class chatWithAiState(StatesGroup):
    chatName = State()
