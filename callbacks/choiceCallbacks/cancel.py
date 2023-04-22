from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers.chatCommands.cancelCommand import cancel
from middlewares.inCreateDialog import createCallbackQuery

router = Router()
router.callback_query.middleware(createCallbackQuery())


@router.callback_query(Text('cancelAi'))
async def cancelCallback(callback: CallbackQuery, state: FSMContext):
    await cancel(callback, state)
    await callback.answer()
