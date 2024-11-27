from loguru import logger

from pydantic import SecretStr, PostgresDsn

from pydantic_settings import BaseSettings, SettingsConfigDict

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from ..utils.read_yaml import read_views


class Settings(BaseSettings):
    telegram_bot_api_token: SecretStr
    data_base_url: PostgresDsn

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()


quiz_bot = Bot(token=settings.telegram_bot_api_token.get_secret_value(), default=DefaultBotProperties(parse_mode='HTML'))

logger_quiz = logger

async_engine = create_async_engine(url=settings.data_base_url.unicode_string())

async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)

views = read_views()
