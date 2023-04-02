from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from callbacks.choiceChat.callbacksFactory import CallbackFactoryForChoiceChat
from middlewares.inCreateDialog import createCallbackQuery
from middlewares.inChatDialog import aiCallbackQuery
from handlers.chatCommands.deleteCommand.deleteChat import deleteChatDelete

router = Router()
router.callback_query.middleware(createCallbackQuery())
router.callback_query.middleware(aiCallbackQuery())


@router.callback_query(CallbackFactoryForChoiceChat.filter(F.action == 'delete'))
async def deleteCallback(
        callback: CallbackQuery,
        callback_data: CallbackFactoryForChoiceChat,
        state: FSMContext
):
    await deleteChatDelete(callback, callback_data, state)
