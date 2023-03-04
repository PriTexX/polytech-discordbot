import discord
from discord import ui, app_commands
from datetime import datetime


# class client(discord.Client):
#     def __init__(self):
#         super().__init__()
#         self.synced = False

class client(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.synced = False


class my_modal(ui.Modal, title="Greeting window"):
    answer = ui.TextInput(label="Enter your Login: ", style=discord.TextStyle.short, placeholder='login@mail.ru',
                          default="login", required=True, max_length=15)

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title=self.title, description=f"**{self.answer.label}**\n{self.answer}",
                              timestamp=datetime.now(), color=discord.Color.blue())
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=embed)


aclient = client()
tree = app_commands.CommandTree(aclient)


@tree.command(guild=discord.Object(id=1073867799451160588), name='modal', description='An example window')
async def modal(interaction: discord.Interaction):
    await interaction.response.send_modal(my_modal())


aclient.run('9d6b443b2f278e3168978d2f390570b82d6d9a4598b8f074a523dcb9a2fba05a')
