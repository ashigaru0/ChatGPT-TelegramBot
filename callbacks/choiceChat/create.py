from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers.chatCommands.cancelCommand import cancel
from middlewares.inChatDialog import aiCallbackQuery

router = Router()
router.callback_query.middleware(aiCallbackQuery())


@router.callback_query(Text('cancelCreate'))
async def cancelCallback(callback: CallbackQuery, state: FSMContext):
    await cancel(callback, state)
    await callback.answer()
