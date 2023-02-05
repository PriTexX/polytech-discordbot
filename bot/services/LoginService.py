from abc import ABC, abstractmethod
from model import LoggedInUser


class LoginService(ABC):

    @abstractmethod
    async def login(self, login: str, password: str) -> LoggedInUser:
        pass
