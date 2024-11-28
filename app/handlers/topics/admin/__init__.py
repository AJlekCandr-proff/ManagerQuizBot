from aiogram import Router

from .handler_addition_task import router as router_addition_task


router = Router(name=__name__)


router.include_routers(router_addition_task)
