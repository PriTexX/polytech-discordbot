from typing import List
import discord


class RoleSortStruct:
    def __init__(self, level, year_number, direction, group_number, role):
        self.direction = direction
        self.year_number = year_number
        self.level = level
        self.group_number = group_number
        self.role = role


def sortRoles(roles: List[discord.Role]) -> List[discord.Role]:
    parameters = []
    sorted_roles = []

    for role in roles:
        level = int(role.name[2:3])
        number_year = int(role.name[:2])
        direction = int(role.name[4:6])
        number = int(role.name[6:])
        role_to_sort = RoleSortStruct(level, number_year, direction, number, role)
        parameters.append(role_to_sort)

    parameters.sort(key=lambda l: l.group_number)
    parameters.sort(key=lambda k: k.direction)
    parameters.sort(key=lambda k: k.year_number)
    parameters.sort(key=lambda s: s.level, reverse=True)

    for sorted_role in parameters:
        sorted_roles.append(sorted_role.role)

    return sorted_roles
