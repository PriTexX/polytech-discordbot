import asyncio
import asyncpg
from aiohttp import ClientSession
import aiohttp
from pathlib import Path
from repository.dao import UserDAO
import logging
from datetime import datetime
from Bot import Bot


async def main():
    from config import TOKEN, DSN

    Path("./logs").mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger('discord')
    logger.setLevel(logging.ERROR)

    current_date = datetime.now().strftime("%Y-%m-%d")
    handler = logging.FileHandler(f"./logs/log_discord_{current_date}.txt")

    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    async with ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as client, asyncpg.create_pool(dsn=DSN, command_timeout=60) as pool:
        async with Bot(client, UserDAO(pool)) as bot:
            await bot.start(TOKEN)


if __name__ == '__main__':
    asyncio.run(main())
