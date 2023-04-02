from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from callbacks.choiceChat.callbacksFactory import CallbackFactoryForChoiceChat
from keyboards.chatActions import getKeyboardChatChoice
from sqlCommands.deleteCommands import deleteChat
from sqlCommands.selectCommands import getChat


async def deleteChatDelete(
        callback: CallbackQuery,
        callback_data: CallbackFactoryForChoiceChat,
        state: FSMContext
):
    userId = callback.message.chat.id
    chats = getChat(userId)
    if chats:
        deleteChat(userId, chats[callback_data.num])
        chats = getChat(userId)
        if chats:
            await callback.message.edit_reply_markup(reply_markup=getKeyboardChatChoice(getChat(userId), 'delete'),
                                                     inline_message_id=str(callback.message.message_id))
        else:
            await callback.message.delete()
    await callback.answer()
