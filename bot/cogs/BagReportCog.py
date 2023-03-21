import discord
from discord.ext import commands
from discord import app_commands
from services import sendBagReport
from core.entity import BagReport


class BagReportCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Отправит ваше сообщение об ошибке для его дальнейшего анализа.")
    @app_commands.describe(full_name='ФИО')
    @app_commands.describe(group='Учебная группа')
    @app_commands.describe(description='Описание ошибки')
    async def report_bag(self, interaction: discord.Interaction, full_name: str, group: str, description: str):
        bag_report = BagReport(full_name, group, interaction.user, interaction.guild.name, description)
        await sendBagReport(interaction, bag_report)


async def setup(bot):
    await bot.add_cog(BagReportCog(bot))
