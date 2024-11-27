from aiogram import Router

from .handler_start import router as router_cmd_start
from .handler_registration import router as router_registration


router = Router(name=__name__)


router.include_routers(router_cmd_start, router_registration)
