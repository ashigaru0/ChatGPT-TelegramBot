from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from utils.getMessage import getMessage

router = Router()


@router.message(Command('cancel'))
async def cancel(message: Message or CallbackQuery, state: FSMContext):
    messageType = getMessage(message)

    if await state.get_state() == 'chatWithAiState:chatName':
        data = await state.get_data()
        await messageType.answer(f'Вы вышли из чата {data["chatName"]}.')
        await state.clear()
    elif await state.get_state() == 'createChatState:choiceName':
        await messageType.answer('Вы вышли из диалога создания чата.')
        await state.clear()
