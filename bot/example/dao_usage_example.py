from repository.dao.user_dao import UserDAO
from repository.entity.user_entity import UserEntity
import random
import asyncpg
import asyncio
from config.config import DSN


async def run():
    async with asyncpg.create_pool(dsn=DSN, command_timeout=60) as pool:
        user_dao = UserDAO(pool)
        users = await user_dao.get_all_users()

        print("Получаем всех пользаков")
        for user in users:
            print(user)

        user = await user_dao.get_user(1)
        print("Получаем пользователя который есть " + str(user))

        user = await user_dao.get_user(4)
        print("Получаем пользователя которого нет " + str(user))

        rows = await user_dao.save_user(UserEntity(1, 'ab80cb36-6c80-4ba8-84fb-823eb7da28a5'))
        print("Insert User пользователь существут поэтому ждем False -> " + str(rows))

        rows = await user_dao.save_user(UserEntity(random.randint(1000, 100000), 'ab80cb36-6c80-4ba8-84fb-823eb7da28a5'))
        print("Insert User пользователь не существут поэтому ждем True -> " + str(rows))


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
