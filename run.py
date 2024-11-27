from asyncio import run

from aiogram import Bot, Dispatcher

from app.configuration.settings import logger_quiz, quiz_bot
from app import router as router_root_project


async def start(bot: Bot) -> None:
    """
    Главная асинхронная функция запуска программы.

    :param bot: Объект класса Bot.
    """

    dp = Dispatcher()
    dp.include_router(router_root_project)

    logger_quiz.info('Bot is started!')

    try:
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        run(start(quiz_bot))

    except KeyboardInterrupt:
        logger_quiz.info('Bot is stopped!')
