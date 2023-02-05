from services import LoginService
from model import LoggedInUser


class LKLoginService(LoginService):

    async def login(self, login: str, password: str) -> LoggedInUser:
        return LoggedInUser("Иван Иванов")
