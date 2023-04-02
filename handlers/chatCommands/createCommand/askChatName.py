from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from handlers.chatCommands.createCommand.askNameStateClass import createChatState
from keyboards.chatActions import getKeyboardForCancel
from middlewares.inChatDialog import aiMessage
from middlewares.inCreateDialog import createMessage
from sqlCommands.selectCommands import getChat

router = Router()
router.message.middleware(createMessage())
router.message.middleware(aiMessage())


@router.message(Command('create'))
async def createGetName(question: Message or CallbackQuery, state: FSMContext):
    questionFrom = question
    if isinstance(question, CallbackQuery):
        questionFrom = question.message
    if len(getChat(questionFrom.chat.id)) < 4:
        await questionFrom.answer('Введите желаемое название чата.\n'
                                  'Не <b>более</b> 20 символов.\n'
                                  'Отменить создание чата можно при вводе команды /cancel или нажатии кнопки ниже.\n\n'
                                  'Возможно создать не более четырёх чатов.',
                                  reply_markup=getKeyboardForCancel('cancelCreate'))
        await state.set_state(createChatState.choiceName)
    else:
        await questionFrom.answer('Достигнут порог количества чатов.\n')
