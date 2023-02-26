import discord


async def createrole(ctx, name: str, color: int):
    mas_roles = ["211-723", "211-729"] #вместо этого, все группы, которые уже есть на сервере
    if mas_roles.indexOf(name) == -1:
        guild = ctx.guild
        role = await guild.create_role(name=name, colour=discord.Colour(color))
        mas_roles.push(role)