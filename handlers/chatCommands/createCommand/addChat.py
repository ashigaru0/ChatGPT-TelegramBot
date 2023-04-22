from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from SQLCommands.insertCommands import addChat
from SQLCommands.selectCommands import getChat
from middlewares.inChatDialog import aiMessage

router = Router()
router.message.middleware(aiMessage())


@router.message(F.text)
async def createAddChat(message: Message, state: FSMContext):
    if await state.get_state() == 'createChatState:choiceName':
        if len(message.text) <= 20:
            if message.text not in await getChat(message.chat.id):
                await addChat(message.chat.id, message.text)
                await state.clear()
                await message.answer('Чат успешно добавлен.')
            else:
                await message.answer('Чат с таким название уже существует.\n'
                                     'Введите желаемое название чата еще раз.')
        else:
            await message.answer('Введенное название чата имеет длину <b>более</b> 20 символов.\n'
                                 'Введите желаемое название чата еще раз.')
