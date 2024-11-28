from aiogram import Router

from .commands import router as router_commands
from .topics import router as router_sections


router = Router(name=__name__)


router.include_routers(router_commands, router_sections)
