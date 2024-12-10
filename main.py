import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.enums import ParseMode
from django.conf import settings

from config.dispatcher import TOKEN
import os
import django

# Set the default settings module for your Django project

def setup_django():
    if not settings.configured:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                              "config.settings")
        django.setup()

async def main() -> None:
    setup_django()
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())