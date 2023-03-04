import discord
from discord.ext import commands
from services import LKLoginService
import os


class Bot(commands.Bot):
    def __init__(self, test_guild_id=None):
        self.testing_guild_id = test_guild_id
        intents = discord.Intents.default()
        intents.emojis = False
        intents.message_content = True
        intents.integrations = False
        intents.webhooks = True
        intents.dm_reactions = False
        intents.guild_reactions = False
        intents.presences = False
        intents.members = True

        self.login_service = LKLoginService()

        super().__init__(command_prefix='!', intents=intents)

    async def setup_hook(self) -> None:
        await self.__load_extensions()

        if self.testing_guild_id:
            guild = discord.Object(self.testing_guild_id)
            # We'll copy in the global commands to test with:
            self.tree.copy_global_to(guild=guild)
            # followed by syncing to the testing guild.
            await self.tree.sync(guild=guild)

    async def __load_extensions(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")