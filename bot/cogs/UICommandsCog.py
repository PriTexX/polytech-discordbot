from discord.ext import commands
from discord import app_commands
from ui import LoginButtonComponent


class UICommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.default_permissions()
    @app_commands.guild_only()
    async def login_button(self, ctx):
        button = LoginButtonComponent()
        await ctx.response.send_message(view=button)


async def setup(bot):
    await bot.add_cog(UICommandsCog(bot))