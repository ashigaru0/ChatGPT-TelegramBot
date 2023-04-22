from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from SQLCommands.selectCommands import getChat
from keyboards.chatActions import getKeyboardChatChoice
from middlewares.inChatDialog import aiMessage
from middlewares.inCreateDialog import createMessage
from utils.getMessage import getMessage

router = Router()
router.message.middleware(createMessage())
router.message.middleware(aiMessage())


@router.message(Command('choice'))
async def choice(message: Message or CallbackQuery):
    messageType = getMessage(message)
    chats = await getChat(messageType.chat.id)
    if chats:
        await messageType.answer('Выберите необходимый чат.',
                                 reply_markup=getKeyboardChatChoice(chats, 'choice'))
    else:
        await messageType.answer('У вас нет созданных чатов.')
