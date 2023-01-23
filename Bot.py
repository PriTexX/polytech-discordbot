import discord
from discord.ext import commands
from infrastructure.services import LKAuthService
import os


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.emojis = False
        intents.integrations = False
        intents.webhooks = True
        intents.dm_reactions = False
        intents.guild_reactions = False
        intents.presences = False
        intents.members = True

        self.auth_service = LKAuthService()

        super().__init__(command_prefix='!', intents=intents)

    async def setup_hook(self) -> None:
        await self.__load_extensions()

    async def __load_extensions(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")