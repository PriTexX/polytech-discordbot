import discord
from discord import ui

from services import LoginService


class LoginModalComponent(ui.Modal, title="Окно авторизации"):
    def __init__(self):
        super().__init__()
        self.interaction: discord.Interaction = None
        self.timeout = 60

    loginInput = ui.TextInput(label="Введите логин: ", style=discord.TextStyle.short, placeholder='i.i.ivanov', required=True, max_length=25)
    passwordInput = ui.TextInput(label="Введите пароль: ", placeholder="Stud123456!", required=True, max_length=20)

    async def on_submit(self, interaction: discord.Interaction):
        self.interaction = interaction
        self.stop()
        # await interaction.response.send_message(f"{logged_in_user.server_name}")
