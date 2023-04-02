from os import remove

from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from middlewares.inCreateDialog import createMessage
from openAiRequests.ChatGPT import makeRequest
from openAiRequests.Whisper import speechToText

router = Router()
router.message.middleware(createMessage())


@router.message(F.text)
async def textDialog(message: Message, state: FSMContext):
    if await state.get_state() == 'chatWithAiState:chatName':
        data = await state.get_data()
        chatName = data['chatName']
        await message.answer(await makeRequest(message.text, chatName, message.chat.id), parse_mode='Markdown')


@router.message(F.voice)
async def audioDialog(message: Message, state: FSMContext, bot: Bot):
    if await state.get_state() == 'chatWithAiState:chatName':
        if message.voice.duration <= 120:
            data = await state.get_data()
            chatName = data['chatName']

            await bot.download(message.voice, destination=f'voice/ogg/{message.voice.file_id}.ogg')
            await message.answer(
                await makeRequest(await speechToText(message.voice.file_id), chatName, message.chat.id),
                parse_mode='Markdown')

            remove(f'voice/ogg/{message.voice.file_id}.ogg')
            remove(f'voice/wav/{message.voice.file_id}.wav')
        else:
            await message.answer('Голосовое сообщение более двух минут.')
