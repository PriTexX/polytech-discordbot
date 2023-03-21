from discord import app_commands
from discord.ext import commands

from ui import LoginButtonComponent, BagReportButtonComponent


class UICommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Разместит кнопку авторизации в чате, из которого вызвана.")
    @app_commands.default_permissions()
    @app_commands.guild_only()
    async def login_button(self, ctx):
        button = LoginButtonComponent(self.bot.login_service)
        await ctx.response.send_message(view=button)

    @app_commands.command(description="Разместит кнопку 'Сообщение об ошибке' в чате, из которого вызвана.")
    @app_commands.default_permissions()
    @app_commands.guild_only()
    async def bag_report_button(self, ctx):
        button = BagReportButtonComponent()
        await ctx.response.send_message(view=button)


async def setup(bot):
    await bot.add_cog(UICommandsCog(bot))
