import asyncio
from aiohttp import ClientSession
from logger import LoggerFactory
from repository.dao import UserDAO
from Bot import Bot


async def main():
    from config.config import TOKEN

    async with ClientSession() as client:
        async with Bot(client, None, test_guild_id=879925656396378112) as bot:
            await bot.start(TOKEN)


if __name__ == '__main__':
    asyncio.run(main())
