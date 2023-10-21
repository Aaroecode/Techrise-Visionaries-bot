from typing import Union
import discord


class RoleNotFound(Exception):
    def __init__(self, role: Union[str, discord.Role, None] = None, message: Union[str, None] = None ):
        if isinstance(role, discord.Role):
            role = role.name
        self.role = role
        self.message = message
        super().__init__(self.role, self.message)

class UserNotFound(Exception):
    def __init__(self, user: Union[str, discord.Role, None] = None, message: Union[str, None] = None ):
        if isinstance(user, discord.User):
            user = user.name
        self.user = user
        self.message = message
        super().__init__(self.user, self.message)
