from loguru import logger

from pydantic import SecretStr

from pydantic_settings import BaseSettings, SettingsConfigDict

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties


class Settings(BaseSettings):
    telegram_bot_api_token: SecretStr

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()


quiz_bot = Bot(token=settings.telegram_bot_api_token.get_secret_value(), default=DefaultBotProperties(parse_mode='HTML'))

logger_quiz = logger
