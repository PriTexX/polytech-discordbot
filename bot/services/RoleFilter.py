from typing import List
import discord


class RoleFilter:
    def __init__(self, role, position):
        self.role = role
        self.position = position


def filterRoles(roles: List[discord.Role]) -> List[discord.Role]:
    cleared_roles = []
    for role in roles:
        position = int(role.position)
        role_to_filter = RoleFilter(position)
        position.append(role_to_filter)

    cleared_roles = [role for role in position if role.isdigit()]
    return cleared_roles.sort(lambda x: x.position)