from aiogram import Router

from .user import router as router_user
from .admin import router as router_admin


router = Router(name=__name__)


router.include_routers(router_user, router_admin)
