from aiogram import Router

from .handlers import router as router_handlers


router = Router(name=__name__)


router.include_router(router_handlers)
