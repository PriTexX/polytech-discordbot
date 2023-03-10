import discord
from math import sin, cos, e
from .RoleSorting import sortRoles


class RoleService:
    async def getOrCreateRole(self, guild: discord.Guild, role_name: str) -> discord.Role:
        role = discord.utils.find(lambda r: r.name == role_name, guild.roles)

        if role:
            return role

        number_year = int(role_name[:2])
        color = discord.Color.from_rgb(int(sin(number_year * 1.43) * 127 + 127),
                                       int(cos(number_year * e ** 3.31) * 127 + 127),
                                       int(sin(number_year * e ** 10.55) * 127 + 127))

        role = await guild.create_role(name=role_name, color=color, hoist=True, mentionable=True,
                                       reason="Created by bot")
        return role
