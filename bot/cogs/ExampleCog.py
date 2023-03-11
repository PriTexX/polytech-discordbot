from discord.ext import commands
from logger import LoggerFactory


class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = LoggerFactory.getLogger(__name__)

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")

    @commands.command()
    async def test(self, ctx):
        self.logger.info("fff")
        await ctx.channel.send("Test command was invoked")


async def setup(bot):
    await bot.add_cog(ExampleCog(bot))
