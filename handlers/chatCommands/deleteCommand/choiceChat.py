from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.chatActions import getKeyboardChatChoice
from middlewares.inCreateDialog import createMessage
from middlewares.inChatDialog import aiMessage
from sqlCommands.selectCommands import getChat

router = Router()
router.message.middleware(createMessage())
router.message.middleware(aiMessage())


@router.message(Command('delete'))
async def deleteChoiceChat(question: Message or CallbackQuery, state: FSMContext):
    questionFrom = question
    if isinstance(question, CallbackQuery):
        questionFrom = question.message
    chats = getChat(questionFrom.chat.id)
    if chats:
        await questionFrom.answer('Выберите необходимый чат для удаления.',
                                reply_markup=getKeyboardChatChoice(chats, 'delete'))
    else:
        await questionFrom.answer('У вас нет созданных чатов.')
