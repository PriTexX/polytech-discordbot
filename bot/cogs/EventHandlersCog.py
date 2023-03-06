from discord import ui
from discord.ext import commands

from bot.ui.discordModal import LoginModal


class EventHandlersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # inside the function describes the creation of view calling
    # LoginModal after clicking on the button,
    # the button can be removed :)
    async def on_member_join(member):
        view = ui.View()
        modal = LoginModal()
        view.add_item(ui.Button(label="Click me", custom_id="my_button", row=0))
        await modal.start(member=member, view=view)


async def setup(bot):
    await bot.add_cog(EventHandlersCog(bot))
