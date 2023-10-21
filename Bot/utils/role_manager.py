import discord
from typing import Union
from Bot.assets import errors
from discord.ext import commands

class roles():
    def __init__(self,client: commands.Bot, guild: Union[str, discord.Guild]):
        if isinstance(guild, str):
            guild = discord.utils.get(client.guilds, name=guild)
        self.client = client
        self.guild = guild
    
    async def add_role(self, role: Union[str, int, discord.role()], user: Union[int, discord.user()], exist_ok: bool = False):
        if isinstance(role, str):
            fetched_role = discord.utils.get(self.guild.roles, name= role)
        
        elif isinstance(role, int):
            fetched_role = discord.utils.get(self.guild.roles, id= role)
        if fetched_role == None:
            raise errors.RoleNotFound(role)
        if exist_ok is True:
            fetched_role = await self.guild.create_role(name = fetched_role, color= discord.Color.green)

        if isinstance(user, int):
            fetched_user = discord.utils.get(self.guild.members, id= user)
        if fetched_user == None and exist_ok is False:
            raise errors.UserNotFound(user)
        await fetched_user.add_roles(role)
    
    async def remove_role(self, role: Union[str, int, discord.role()], user: Union[int, discord.user()]):
        if isinstance(role, str):
            fetched_role = discord.utils.get(self.guild.roles, name= role)
        
        elif isinstance(role, int):
            fetched_role = discord.utils.get(self.guild.roles, id= role)
        if fetched_role == None:
            raise errors.RoleNotFound(role)
        if isinstance(user, int):
            fetched_user = discord.utils.get(self.guild.members, id= user)
        if fetched_user == None:
            raise errors.UserNotFound(user)
        await fetched_user.remove_roles(role)
         

        
        
