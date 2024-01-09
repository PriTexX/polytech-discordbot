import re

import discord

from repository.entity import UserEntity
from core.errors import WrongUsernameOrPasswordException
from logger import LoggerFactory
from services import AuthService, RoleService
from ui import LoginModalComponent


class LoginService:
    def __init__(self, auth_service: AuthService, role_service: RoleService):
        self.logger = LoggerFactory.getLogger(__name__)
        self.login_service: AuthService = auth_service
        self.role_service = role_service

    async def login(self, interaction: discord.Interaction) -> None:
        modal = LoginModalComponent()
        await interaction.response.send_modal(modal)

        if await modal.wait():  # Вернет False при timeout или если пользователь закроет окно
            return

        try:
            authenticated_user = await self.login_service.authenticate(modal.loginInput, modal.passwordInput)

        except WrongUsernameOrPasswordException:
            await modal.interaction.response.send_message("Неверный логин или пароль. Попробуйте ещё раз.",
                                                          ephemeral=True, delete_after=120)
            return

        except Exception:
            self.logger.exception("Unhandled exception during lk api calls")
            await modal.interaction.response.send_message("Неизвестная ошибка на сервере. Попробуйте ещё раз позже.",
                                                          ephemeral=True, delete_after=120)
            return

        if not re.fullmatch("09.0[346].0[12]", authenticated_user.department_code):
            await modal.interaction.response.send_message(
                "Ваш код специальности должен быть 09.03.02, 09.04.02 либо 09.06.01 чтобы авторизоваться на данном сервере.",
                ephemeral=True, delete_after=120)

        students_role = discord.utils.find(lambda r: r.name == "student", interaction.guild.roles)
        user_role, role_is_new = await self.role_service.getOrCreateRole(interaction.guild, authenticated_user.group)

        user_roles = interaction.user.roles

        role_pattern = "\d+-\d+"
        for role in user_roles:
            if re.fullmatch(role_pattern, role.name):
                await interaction.user.remove_roles(role)

        await interaction.user.add_roles(students_role, user_role)
        await interaction.user.edit(nick=authenticated_user.server_name)

        await modal.interaction.response.send_message(
            f"Вы успешно авторизованы {authenticated_user.server_name.split()[1]}",
            ephemeral=True, delete_after=120)

        try:
            await interaction.client.user_repository.saveOrUpdateUser(
                UserEntity(interaction.user.id, authenticated_user.guid))

        except Exception:
            self.logger.exception("Error during saving user's info")

        if role_is_new:
            self.logger.info(f"Correcting roles positions with new role: {user_role.name}")
            await self.role_service.correctRolesPositions(interaction.guild)
