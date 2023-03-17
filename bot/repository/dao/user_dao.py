from typing import List, Union

from .abstract_dao import AbstractDAO
from repository.entity import UserEntity

SELECT_ALL_USERS = 'SELECT discorduserid, onecguid FROM discordstudents'
SELECT_USER = 'SELECT discorduserid, onecguid FROM discordstudents WHERE discorduserid = $1'
INSERT_USER = 'INSERT INTO discordstudents(discorduserid, onecguid) VALUES ($1, $2)'
UPDATE_USER = 'UPDATE discordstudents SET onecguid = $1 WHERE discorduserid = $2'


class UserDAO(AbstractDAO):

    async def getAllUsers(self) -> List[UserEntity]:
        result = await self._pool.fetch(SELECT_ALL_USERS)
        users = []
        for user_record in result:
            users.append(UserEntity(user_record['discorduserid'], user_record['onecguid']))
        return users

    async def getUser(self, user_id: int) -> Union[UserEntity, None]:
        result = await self._pool.fetchrow(SELECT_USER, user_id)
        if result is None:
            return None
        return UserEntity(result['discorduserid'], result['onecguid'])

    async def saveUser(self, user: UserEntity) -> bool:
        remote_user = await self.getUser(user.id)
        if not remote_user:
            await self._pool.execute(INSERT_USER, user.id, user.external_id)
            return True
        return False

    async def updateUser(self, user: UserEntity) -> UserEntity:
        await self._pool.execute(UPDATE_USER, user.external_id, user.id)
        return user

    async def saveOrUpdateUser(self, user: UserEntity) -> UserEntity:
        user_exists = not (await self.saveUser(user))

        if user_exists:
            await self.updateUser(user)

        return user

