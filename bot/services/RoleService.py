import re

import discord
from typing import Tuple
from math import sin, cos, e
from .RoleSorting import sortRoles


def createRolesToPositionsDict(filtered_roles):
    max_position = max([role.position for role in filtered_roles])
    sorted_roles = sortRoles(filtered_roles)

    roles_to_positions_dict = {}

    current_position = max_position
    for role in sorted_roles:
        roles_to_positions_dict[role] = current_position
        current_position -= 1

    return roles_to_positions_dict


class RoleService:
    async def getOrCreateRole(self, guild: discord.Guild, role_name: str) -> Tuple[discord.Role, bool]:
        is_new = False
        role = discord.utils.find(lambda r: r.name == role_name, guild.roles)

        if role:
            return role, is_new

        number_year = int(role_name[:2])
        color = discord.Color.from_rgb(int(sin(number_year * 1.43) * 127 + 127),
                                       int(cos(number_year * e ** 3.31) * 127 + 127),
                                       int(sin(number_year * e ** 10.55) * 127 + 127))

        role = await guild.create_role(name=role_name, color=color, hoist=True, mentionable=True,
                                       reason="Created by bot")
        is_new = True
        return role, is_new

    async def correctRolesPositions(self, guild: discord.Guild) -> None:
        roles = await guild.fetch_roles()
        filtered_roles = [role for role in roles if re.fullmatch("[0-9]+-[0-9]{1,4}", role.name)]
        roles_to_positions_dict = createRolesToPositionsDict(filtered_roles)
        await guild.edit_role_positions(roles_to_positions_dict)
