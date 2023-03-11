import discord
from ui import LoginModalComponent


class LoginButtonComponent(discord.ui.View):
    def __init__(self, login_service):
        super().__init__(timeout=None)
        self.login_service = login_service

    @discord.ui.button(label="Авторизация", style=discord.ButtonStyle.primary, custom_id="auth-btn")
    async def button_click(self, interaction, button):
        await interaction.response.send_modal(LoginModalComponent(self.login_service))
