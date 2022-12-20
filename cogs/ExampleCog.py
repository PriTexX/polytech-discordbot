from discord.ext import commands


class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")

    @commands.command()
    async def test(self, ctx):
        await ctx.channel.send("Test command was invoked")


def setup(bot):
    bot.add_cog(ExampleCog(bot))
