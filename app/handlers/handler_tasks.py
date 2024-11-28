from aiogram import Router
from aiogram.types import Message

from ..filters.filters_tasks import TasksFilter
from ..configuration.settings import views
from ..middlewares.is_registered_middleware import UserRegisteredMiddleware
from ..database.CRUDs.select_user import select_user


router = Router(name=__name__)

router.message.middleware(UserRegisteredMiddleware())


@router.message(TasksFilter())
async def handler_tasks(message: Message) -> None:
    """
    Асинхронный обработчик нажатия кнопки "".
    Присылает задания для определенной школы (категории),
    в которой находится ученик.

    :param message: Объект класса Message.
    """

    user = await select_user(message.from_user.id)

    await message.answer(
        text=f"{user.name}, {views.get('tasks_view')}\n "
             f"<b>Твоя категория:</b> {user.category}\n"
             f"<b>🏅 Твои баллы:</b> <code>{user.points}</code>",
    )
