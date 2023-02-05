from abc import ABC, abstractmethod
from model import AuthenticatedUser


class AuthService(ABC):

    @abstractmethod
    async def authenticate(self, login: str, password: str) -> AuthenticatedUser:
        pass
