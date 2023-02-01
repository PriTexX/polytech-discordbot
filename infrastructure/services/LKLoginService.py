from abstract.services import LoginService
from core.entities import LoggedInUser


class LKLoginService(LoginService):

    async def login(self, login: str, password: str) -> LoggedInUser:
        return LoggedInUser("Иван Иванов")
