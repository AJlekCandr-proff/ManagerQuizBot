from typing import Awaitable, Any, Dict, Callable

from aiogram.types import Message
from aiogram.dispatcher.middlewares.base import BaseMiddleware

from ..database.CRUDs.select_user import select_user
from ..configuration.settings import views


class UserNotRegisteredMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[
                [Message, Dict[str, Any]],
                Awaitable[Any]
            ],
            message: Message,
            data: Dict[Any, str | Dict[str, Any]],
    ) -> None:
        user = await select_user(message.from_user.id)

        if user:
            return await message.answer(text=views.get('error_registration'))

        else:
            return await handler(message, data)
