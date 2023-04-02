from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.chatActions import getKeyboardOutDialog
from middlewares.inCreateDialog import createMessage
from middlewares.inChatDialog import aiMessage
from sqlCommands.insertCommands import addUser

router = Router()
router.message.middleware(createMessage())
router.message.middleware(aiMessage())


@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    addUser(message.from_user.id)
    await message.answer('👋 Здравствуйте! <b>ChatGPTbot</b> — это бот, использующий нейросеть <b>ChatGPT</b>, '
                         'этот бот даст вам ответ на любые интересующие вас вопросы.\n\n'
                         'Бот может принимать вопросы в виде текста, так и в виде аудио благодаря '
                         'нейросети <b>Whisper</b>.\n\n'
                         'Больше информации о командах в /help.', reply_markup=getKeyboardOutDialog())


@router.message(Command('help'))
async def start(message: Message, state: FSMContext):
    await message.answer('/create - <b>Cоздать</b> чат.\n'
                         '/delete - <b>Удалить</b> чат.\n'
                         '/choice - <b>Выбрать</b> чат')
