from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.chatActions import getKeyboardOutDialog
from middlewares.inCreateDialog import createMessage
from middlewares.inChatDialog import aiMessage
from SQLCommands.insertCommands import addUser

router = Router()
router.message.middleware(createMessage())
router.message.middleware(aiMessage())


@router.message(Command('start'))
async def start(message: Message):
    await addUser(message.from_user.id)
    await message.answer('👋 Здравствуйте! <b>ChatGPTbot</b> — это бот, использующий нейросеть <b>ChatGPT</b>, '
                         'который даст вам ответ на любые интересующие вас вопросы.\n\n'
                         'Бот может принимать вопросы в виде текста, так и в виде голосового сообщения благодаря '
                         'нейросети <b>Whisper</b>.\n\n'
                         'Больше информации о командах в /help.', reply_markup=getKeyboardOutDialog())


@router.message(Command('help'))
async def start(message: Message):
    await message.answer('/create - Cоздать чат.\n'
                         '/delete - Удалить чат.\n'
                         '/choice - Выбрать чат.\n'
                         '/cancel - Выйти из диалога.\n'
                         '/start - Главное меню.\n'
                         '/help - Информация о командах.')
