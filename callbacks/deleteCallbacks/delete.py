from aiogram import F
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from SQLCommands.deleteCommands import deleteChat
from SQLCommands.selectCommands import getChat
from callbacks.callbacksFactory import CallbackFactoryForChoiceChat
from keyboards.chatActions import getKeyboardChatChoice
from middlewares.inChatDialog import aiCallbackQuery
from middlewares.inCreateDialog import createCallbackQuery

router = Router()
router.callback_query.middleware(createCallbackQuery())
router.callback_query.middleware(aiCallbackQuery())


@router.callback_query(CallbackFactoryForChoiceChat.filter(F.action == 'delete'))
async def deleteChatDelete(
        callback: CallbackQuery,
        callback_data: CallbackFactoryForChoiceChat
):
    userId = callback.message.chat.id
    chats = await getChat(userId)
    if chats:
        await deleteChat(userId, chats[callback_data.num])
        chats = await getChat(userId)
        if chats:
            await callback.message.edit_reply_markup(
                reply_markup=getKeyboardChatChoice(await getChat(userId), 'delete'),
                inline_message_id=str(callback.message.message_id))
        else:
            await callback.message.delete()
    await callback.answer()
