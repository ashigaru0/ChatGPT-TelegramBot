from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from handlers.chatCommands.createCommand.addChat import createAddChat

class createMessage(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        if not await data['state'].get_state() == 'createChatState:choiceName':
            return await handler(event, data)
        return await createAddChat(event, data['state'])


class createCallbackQuery(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        if not await data['state'].get_state() == 'createChatState:choiceName':
            return await handler(event, data)
        return await event.answer()


