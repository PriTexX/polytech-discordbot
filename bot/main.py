import asyncio
from Bot import Bot


async def main():
    from config.config import TOKEN
    bot = Bot()
    await bot.start(TOKEN)


if __name__ == '__main__':
    asyncio.run(main())
