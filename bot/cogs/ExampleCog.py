from datetime import datetime
import discord
from discord import ui
from discord.ext import commands

from UI.discordModal import my_modal


class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")

    bot = commands.Bot(command_prefix="!")

    @bot.event # inside the function describes the creation of view calling my_model after clicking on the button,
    # the button can be removed :)
    async def on_member_join(member):
        view = ui.View()
        modal = my_modal()
        view.add_item(ui.Button(label="Click me", custom_id="my_button", row=0))
        await modal.start(member=member, view=view)


    @commands.command()
    async def test(self, ctx):
        await ctx.channel.send("Test command was invoked")


async def setup(bot):
    await bot.add_cog(ExampleCog(bot))
