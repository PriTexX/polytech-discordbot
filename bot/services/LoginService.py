from logger import LoggerFactory
from core.errors import WrongUsernameOrPasswordException, ServerError
from services import AuthService, RoleService
from ui import LoginModalComponent
import discord


class LoginService:
    def __init__(self, auth_service: AuthService, role_service: RoleService):
        self.logger = LoggerFactory.getLogger(__name__)
        self.login_service: AuthService = auth_service
        self.role_service = role_service

    async def login(self, interaction: discord.Interaction) -> None:
        modal = LoginModalComponent()
        await interaction.response.send_modal(modal)

        if await modal.wait(): # Вернет False при timeout или если пользователь закроет окно
            return

        try:
            authenticated_user = await self.login_service.authenticate(modal.loginInput, modal.passwordInput)
            await modal.interaction.response.send_message(f"Вы успешно авторизованы {authenticated_user.server_name}", ephemeral=True)

        except WrongUsernameOrPasswordException:
            await modal.interaction.response.send_message("Неверный логин или пароль. Попробуйте ещё раз.", ephemeral=True)
            return

        except Exception:
            self.logger.exception("Unhandled exception during lk api calls")
            return


