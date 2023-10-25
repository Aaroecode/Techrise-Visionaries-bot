from discord.ext import commands, tasks
import discord
from itertools import cycle

async def setup(client):
    await client.add_cog(Presence(client))


class Presence(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    status_list = ["Test"]
    status = cycle(status_list)
    loop_time = 10
    
    @tasks.loop(seconds=loop_time)
    async def change_presence(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game(next(self.status)))

    @commands.command(description="Used to Change presence of a bot")
    async def presence(self, ctx, method: str=None, value:str =None):
        if method == "add":
            self.status_list.append(value)
            await ctx.send(f"Successfully added {value} to presence list")

        elif method == "remove":
            try:
                self.status_list.remove(value)
                await ctx.send(f"Remove {value} from presence list")
            except KeyError as e:
                await ctx.send(f"{value} is not a valid presence")
            
        elif method == "time":
            try:
                value = int(value)
                self.loop_time = value
                await ctx.send(f"loop time set to {value} seconds") 
            except ValueError:
                await ctx.send(f"{value} is not a valid")
        else:
            await ctx.send("Invalid method")




