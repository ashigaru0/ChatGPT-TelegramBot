from aiogram.types import Message, CallbackQuery


def getMessage(message: Message or CallbackQuery):
    messageType = message
    if isinstance(message, CallbackQuery):
        messageType = message.message
    return messageType
