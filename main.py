import asyncio
from os import environ

from aiogram import Dispatcher, Bot

from callbacks import chatActions
from callbacks.createCallbacks import create
from callbacks.deleteCallbacks import delete
from callbacks.choiceCallbacks import cancel, choice
from handlers import startCommands
from handlers.chatCommands import createCommand, deleteCommand, choiceCommand, cancelCommand
from handlers.chatCommands.choiceCommand import dialogWithAi


async def main():
    bot = Bot(token=environ.get('TG_CHATGPT_BOT_API'), parse_mode='Html')
    dp = Dispatcher()
    dp.include_router(startCommands.router)
    dp.include_router(cancelCommand.router)
    dp.include_routers(deleteCommand.choiceChat.router)
    dp.include_routers(createCommand.askChatName.router)
    dp.include_router(chatActions.router)
    dp.include_routers(choice.router, delete.router, create.router, cancel.router)
    dp.include_routers(choiceCommand.choiceChat.router, dialogWithAi.router, createCommand.addChat.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
