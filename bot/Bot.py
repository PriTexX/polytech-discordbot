import os

import discord
from aiohttp import ClientSession
from discord.ext import commands

from services import AuthService, LoginService, RoleService
from ui import LoginButtonComponent, BagReportButtonComponent


class Bot(commands.Bot):
    def __init__(self, client: ClientSession, test_guild_id=None):
        self.testing_guild_id = test_guild_id
        intents = discord.Intents.default()
        intents.emojis = False
        intents.message_content = True  # TODO change to false
        intents.integrations = False
        intents.webhooks = True
        intents.dm_reactions = False
        intents.guild_reactions = False
        intents.presences = False
        intents.members = True

        self.me = None  # User object to send messages directly to my personal messages. Will be set in on_ready event

        self.login_service = LoginService(AuthService(client=client), RoleService())

        super().__init__(command_prefix='!', intents=intents)

    async def setup_hook(self) -> None:
        await self.__load_extensions()

        self.add_view(LoginButtonComponent(self.login_service))
        self.add_view(BagReportButtonComponent())

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
