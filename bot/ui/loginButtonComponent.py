import discord
from ui import LoginModalComponent


class LoginButtonComponent(discord.ui.View):
    @discord.ui.button(label="Авторизация", style=discord.ButtonStyle.primary)
    async def button_click(self, interaction, button):
        await interaction.response.send_modal(LoginModalComponent())
