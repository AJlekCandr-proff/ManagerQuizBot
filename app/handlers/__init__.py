from aiogram import Router

from .handler_start import router as router_cmd_start


router = Router(name=__name__)


router.include_routers(router_cmd_start)
