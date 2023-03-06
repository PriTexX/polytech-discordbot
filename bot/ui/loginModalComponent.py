from datetime import datetime

import discord
from discord import ui


class LoginModalComponent(ui.Modal, title="Окно авторизации"):
    answer = ui.TextInput(label="Введите логин: ", style=discord.TextStyle.short, placeholder='i.i.ivanov', required=True, max_length=25)
    answerPass = ui.TextInput(label="Введите пароль: ", placeholder="Stud123456!", required=True, max_length=20)

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title=self.title, description=f"**{self.answer.label}**\n{self.answer}",
                              timestamp=datetime.now(), color=discord.Color.blue())
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=embed)
