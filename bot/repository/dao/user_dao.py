from typing import List

from .abstract_dao import AbstractDAO
from repository.entity.user_entity import UserEntity

SELECT_ALL_USERS = 'SELECT discorduserid, onecguid FROM discordstudents'
SELECT_USER = 'SELECT discorduserid, onecguid FROM discordstudents WHERE discorduserid = %s'
INSERT_USER = 'INSERT INTO discordstudents(discorduserid, onecguid) VALUES (%s, %s)'


class UserDAO(AbstractDAO):

    def get_all_users(self) -> List[UserEntity]:
        result = self._select_many(SELECT_ALL_USERS)
        users = []
        for user_record in result:
            users.append(UserEntity(user_record[0], user_record[1]))
        return users

    def get_user(self, user_id: int) -> UserEntity:
        result = self._select_one(SELECT_USER, (user_id,))
        if result is None:
            return UserEntity()
        return UserEntity(result[0], result[1])

    def save_user(self, user: UserEntity) -> int:
        remote_user = self.get_user(user.id)
        if remote_user.is_empty():
            return self._execute(INSERT_USER, (user.id, user.external_id))
        return 0
