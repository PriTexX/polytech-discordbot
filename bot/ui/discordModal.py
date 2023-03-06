import discord
from discord import ui, app_commands
from datetime import datetime


# # class client(discord.Client):
# #     def __init__(self):
# #         super().__init__()
# #         self.synced = False
#
# class client(discord.Client):
#     def __init__(self):
#         intents = discord.Intents.default()
#         super().__init__(intents=intents)
#         self.synced = False
#
#     async def on_ready(self):
#         await self.wait_until_ready()
#         if not self.synced:
#             await tree.sync(guild=discord.Object(id=1073867799451160588))
#             self.synced = True
#         print("smth")


class LoginModal(ui.Modal, title="Greeting window"):
    answer = ui.TextInput(label="Enter your Login: ", style=discord.TextStyle.short, placeholder='login@mail.ru',
                          default="login", required=True, max_length=15)
    answerPass = ui.TextInput(label="Enter your Password: ", style=discord.TextStyle.short, placeholder='123',
                          default="****", required=True, max_length=20)

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title=self.title, description=f"**{self.answer.label}**\n{self.answer}",
                              timestamp=datetime.now(), color=discord.Color.blue())
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=embed)
        #we display the user's login, the value of the first variable


# aclient = client()
# tree = app_commands.CommandTree(aclient)
#
#
# @tree.command(guild=discord.Object(id=1073867799451160588), name='modal', description='An example window')
# # @bot.slash_command()
# async def modal(interaction: discord.Interaction):
#     await interaction.response.send_modal(LoginModal())
#
#
# aclient.run("MTA3Mzg2Nzc5OTQ1MTE2MDU4OA.GLPUUs.SX_x_kGX0oBDQ1zBfmQSAbmjGA_y4G9ge1cC7o")
