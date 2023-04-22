from aiogram.filters.callback_data import CallbackData


class CallbackFactoryForChoiceChat(CallbackData, prefix="fabnum"):
    action: str
    num: int
