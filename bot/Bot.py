import discord
from discord.ext import commands
from services import AuthService, LoginService, RoleService
from repository.dao import UserDAO
from aiohttp import ClientSession
from ui import LoginButtonComponent
import os


class Bot(commands.Bot):
    def __init__(self, client: ClientSession, repository: UserDAO, test_guild_id=None):
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

        self.user_repository = repository

        self.login_service = LoginService(AuthService(client=client), RoleService())

        super().__init__(command_prefix='!', intents=intents)

    async def setup_hook(self) -> None:
        await self.__load_extensions()

        self.add_view(LoginButtonComponent(self.login_service))

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
