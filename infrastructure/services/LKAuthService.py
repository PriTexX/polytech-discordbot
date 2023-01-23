from abstract.services import AuthService
from core.entities import AuthenticatedUser


class LKAuthService(AuthService):

    async def authenticate(self, login: str, password: str) -> AuthenticatedUser:
        return AuthenticatedUser("Иванов Иван", "194-321", "09.03.02 Информационные системы и технологии", "ae0c3426-af36-4229-999d-4cabab6c5fba")
