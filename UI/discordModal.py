import discord
from discord import ui, app_commands
from datetime import datetime

from discord.app_commands import tree


class my_modal(ui.Modal, title="Greeting window"):
    answer = ui.TextInput(label="Enter your Login: ", style=discord.TextStyle.short, placeholder='login@mail.ru',
                          default="login", required=True, max_length=15)

@tree.command(guild = discord.Object(id=1073867799451160588), name = 'modal', description='An example window')
async def madal(interaction: discord.Interaction):
    await interaction.response.sen
