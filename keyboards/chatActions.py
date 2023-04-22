from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callbacks.callbacksFactory import CallbackFactoryForChoiceChat


def getKeyboardOutDialog():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text='Выбрать чат', callback_data='choice')
    )
    builder.row(
        InlineKeyboardButton(
            text='Создать чат', callback_data='create'),
        InlineKeyboardButton(
            text='Удалить чат', callback_data='delete')
    )
    return builder.as_markup()


def getKeyboardChatChoice(chats, action):
    builder = InlineKeyboardBuilder()
    for num, chat in enumerate(chats):
        builder.button(text=chat, callback_data=CallbackFactoryForChoiceChat(action=action, num=num))
    return builder.as_markup()


def getKeyboardForCancel(dialog):
    builder = InlineKeyboardBuilder()
    if dialog == 'cancelCreate':
        builder.button(text='Отменить создание чата.', callback_data=dialog)
    elif dialog == 'cancelAi':
        builder.button(text='Выйти из чата.', callback_data=dialog)
    return builder.as_markup()
