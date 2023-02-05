import asyncio
import discord.ext.commands
from Bot import Bot

bot = Bot()


@bot.command()
@discord.ext.commands.has_permissions(administrator=True)
async def load(ctx, extensions):
    await bot.load_extension(f"cogs.{extensions}")
    await ctx.author.send("Done")


@bot.command()
@discord.ext.commands.has_permissions(administrator=True)
async def unload(ctx, extensions):
    await bot.unload_extension(f"cogs.{extensions}")
    await ctx.author.send("Done")


@bot.command()
@discord.ext.commands.has_permissions(administrator=True)
async def reload(ctx, extensions):
    await bot.unload_extension(f"cogs.{extensions}")
    await bot.load_extension(f"cogs.{extensions}")
    await ctx.author.send("Done")


async def main():
    from config.config import TOKEN
    await bot.start(TOKEN)


if __name__ == '__main__':
    asyncio.run(main())
