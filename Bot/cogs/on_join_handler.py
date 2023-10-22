from discord.ext import commands
from Bot.utils import role_manager
from Bot.config.config import Config
import discord

logger = Config.bot_logger

async def setup(client):
    await client.add_cog(onJoin(client))


class onJoin(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
        self.roles = role_manager.roles(self.client, guild=Config.server["Name"])
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        members_role = Config.server["Member_role"]
        try:
            members_role = int(members_role)
        except ValueError:
            pass
        self.roles.add_role(members_role, member, exist_ok=True)
        logger.info(f"Member {member.name} with id {member.id} joined server")


        





        