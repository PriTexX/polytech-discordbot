from repository.dao.user_dao import UserDAO
from repository.entity.user_entity import UserEntity
import random

if __name__ == '__main__':

    with UserDAO() as user_dao:
        users = user_dao.get_all_users()

        print("Получаем всех пользаков")
        for user in users:
            print(user)

        user = user_dao.get_user(1)
        print("Получаем пользователя который есть " + str(user))

        user = user_dao.get_user(4)
        print("Получаем пользователя которого нет " + str(user))

        rows = user_dao.save_user(UserEntity(1, 'ab80cb36-6c80-4ba8-84fb-823eb7da28a5'))
        print("Insert User пользователь существут поэтому ждем 0 -> " + str(rows))

        rows = user_dao.save_user(UserEntity(random.randint(1000, 100000), 'ab80cb36-6c80-4ba8-84fb-823eb7da28a5'))
        print("Insert User пользователь не существут поэтому ждем 1 -> " + str(rows))
