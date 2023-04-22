from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers.chatCommands.choiceCommand.choiceChat import choice
from handlers.chatCommands.createCommand.askChatName import createGetName
from handlers.chatCommands.deleteCommand.choiceChat import deleteChoiceChat
from middlewares.inChatDialog import aiCallbackQuery
from middlewares.inCreateDialog import createCallbackQuery

router = Router()
router.callback_query.middleware(createCallbackQuery())
router.callback_query.middleware(aiCallbackQuery())


@router.callback_query(Text('choice'))
async def choiceCallback(callback: CallbackQuery, state: FSMContext):
    await choice(callback, state)
    await callback.answer()


@router.callback_query(Text('create'))
async def createCallback(callback: CallbackQuery, state: FSMContext):
    await createGetName(callback, state)
    await callback.answer()


@router.callback_query(Text('delete'))
async def deleteCallback(callback: CallbackQuery, state: FSMContext):
    await deleteChoiceChat(callback, state)
    await callback.answer()
