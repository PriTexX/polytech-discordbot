import discord
from discord.ext import commands
import os


class Bot(commands.Bot):
    def __init__(self, token):
        self.token = token

        intents = discord.Intents.default()
        intents.emojis = False
        intents.integrations = False
        intents.webhooks = True
        intents.dm_reactions = False
        intents.guild_reactions = False
        intents.presences = False
        intents.members = True

        super().__init__(command_prefix='!', intents=intents)

    def run(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")
        super().run(self.token)