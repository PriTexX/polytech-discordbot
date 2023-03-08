import discord
from discord import ui

from services import LoginService


class LoginModalComponent(ui.Modal, title="Окно авторизации"):
    def __init__(self, login_service: LoginService):
        super().__init__()
        self.login_service = login_service

    answer = ui.TextInput(label="Введите логин: ", style=discord.TextStyle.short, placeholder='i.i.ivanov', required=True, max_length=25)
    answerPass = ui.TextInput(label="Введите пароль: ", placeholder="Stud123456!", required=True, max_length=20)

    async def on_submit(self, interaction: discord.Interaction):
        logged_in_user = await self.login_service.login(self.answer, self.answerPass)
        await interaction.response.send_message(f"{logged_in_user.server_name}")
