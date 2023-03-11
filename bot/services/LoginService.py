from core.entity import LoggedInUser
from core.errors import WrongUsernameOrPasswordException, ServerError
from services import AuthService, RoleService
import discord


class LoginService:
    def __init__(self, auth_service: AuthService, role_service: RoleService):
        self.login_service: AuthService = auth_service
        self.role_service = role_service

    async def login(self, login, password) -> LoggedInUser:
        try:
            authenticated_user = await self.login_service.authenticate(login, password)
        except WrongUsernameOrPasswordException:
            pass
        except ServerError:
            pass
        except Exception:
            pass



