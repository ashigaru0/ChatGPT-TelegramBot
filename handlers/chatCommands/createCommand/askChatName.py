from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from handlers.chatCommands.createCommand.askNameStateClass import createChatState
from keyboards.chatActions import getKeyboardForCancel
from middlewares.inChatDialog import aiMessage
from middlewares.inCreateDialog import createMessage
from SQLCommands.selectCommands import getChat
from utils.getMessage import getMessage

router = Router()
router.message.middleware(createMessage())
router.message.middleware(aiMessage())


@router.message(Command('create'))
async def createGetName(message: Message or CallbackQuery, state: FSMContext):
    messageType = getMessage(message)
    if len(await getChat(messageType.chat.id)) < 4:
        await messageType.answer('Введите желаемое название чата.\n'
                                  'Не <b>более</b> 20 символов.\n'
                                  'Отменить создание чата можно при вводе команды /cancel или нажатии кнопки ниже.\n\n'
                                  'Возможно создать не более четырёх чатов.',
                                  reply_markup=getKeyboardForCancel('cancelCreate'))
        await state.set_state(createChatState.choiceName)
    else:
        await messageType.answer('Достигнут порог количества чатов.\n')
