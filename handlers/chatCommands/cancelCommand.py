from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

router = Router()


@router.message(Command('cancel'))
async def cancel(answer: Message or CallbackQuery, state: FSMContext):
    answerFrom = answer
    if isinstance(answer, CallbackQuery):
        answerFrom = answer.message

    if await state.get_state() == 'chatWithAiState:chatName':
        data = await state.get_data()
        await answerFrom.answer(f'Вы вышли из чата {data["chatName"]}.')
        await state.clear()
    elif await state.get_state() == 'createChatState:choiceName':
        await answerFrom.answer('Вы вышли из диалога создания чата.')
        await state.clear()
