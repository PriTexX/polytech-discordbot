from discord.ext import commands


class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.me = await self.bot.fetch_user(229033111197843456)

        print("Ready for work")

    @commands.command()
    async def sync(self, ctx):
        if ctx.author.id != self.bot.me.id:
            return

        self.bot.tree.copy_global_to(guild=ctx.guild)
        await self.bot.tree.sync(guild=ctx.guild)
        await self.bot.me.send("Done syncing slash commands")


async def setup(bot):
    await bot.add_cog(EventCog(bot))
