import asyncio
import logging

from aiogram import Bot
from dispatcher import get_dispatcher
from src.config import config
from util.commands_description import register_commands_description


async def start_bot():
    bot: Bot = Bot(config.bot.token)
    # storage = MemoryStorage() # redis storage
    dp = get_dispatcher()
    await register_commands_description(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def main():
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(start_bot())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == "__main__":
    main()