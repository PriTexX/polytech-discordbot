from abc import ABC, abstractmethod
from core.entities import LoggedInUser


class LoginService(ABC):

    @abstractmethod
    async def login(self, login: str, password: str) -> LoggedInUser:
        pass
