from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from SQLCommands.selectCommands import getChat
from callbacks.callbacksFactory import CallbackFactoryForChoiceChat
from handlers.chatCommands.choiceCommand.chatWithAiStateClass import chatWithAiState
from keyboards.chatActions import getKeyboardForCancel
from middlewares.inChatDialog import aiCallbackQuery
from middlewares.inCreateDialog import createCallbackQuery

router = Router()
router.callback_query.middleware(createCallbackQuery())
router.callback_query.middleware(aiCallbackQuery())


@router.callback_query(CallbackFactoryForChoiceChat.filter(F.action == 'choice'))
async def choiceCallback(
        callback: CallbackQuery,
        callback_data: CallbackFactoryForChoiceChat,
        state: FSMContext
):
    userId = callback.message.chat.id
    chats = await getChat(userId)
    await state.set_state(chatWithAiState.chatName)
    await state.update_data(chatName=chats[callback_data.num])
    await callback.message.answer(f'Вы вошли в чат {chats[callback_data.num]}.\n'
                                  f'Вы можете задать ИИ свои вопросы.\n'
                                  f'Вы можете присылать голосовые сообщения не более двух минут.\n\n'
                                  f'Для выхода из чата нажмите кнопку ниже или введите команду /cancel',
                                  reply_markup=getKeyboardForCancel('cancelAi'))
    await callback.answer()
