import discord.ext.commands

from Bot import Bot
from config import TOKEN

bot = Bot(TOKEN)


@bot.command()
@discord.ext.commands.has_permissions(administator=True)
async def load(ctx, extensions):
    await bot.load_extension(f"cogs.{extensions}")
    await ctx.author.send("Done")


@bot.command()
@discord.ext.commands.has_permissions(administator=True)
async def unload(ctx, extensions):
    await bot.unload_extension(f"cogs.{extensions}")
    await ctx.author.send("Done")


@bot.command()
@discord.ext.commands.has_permissions(administator=True)
async def reload(ctx, extensions):
    await bot.unload_extension(f"cogs.{extensions}")
    await bot.load_extension(f"cogs.{extensions}")
    await ctx.author.send("Done")


if __name__ == '__main__':
    bot.run()
