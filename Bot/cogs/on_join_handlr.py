from discord.ext import commands
import discord

class onJoin(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass




async def setup(client):
    await client.add_cog(onJoin(client))
        