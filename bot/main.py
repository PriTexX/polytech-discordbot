import asyncio
from aiohttp import ClientSession
from repository.dao import UserDAO
from Bot import Bot


async def main():
    from config.config import TOKEN

    async with ClientSession() as client, UserDAO() as user_repository:
        async with Bot(client, user_repository) as bot:
            await bot.start(TOKEN)


if __name__ == '__main__':
    asyncio.run(main())
