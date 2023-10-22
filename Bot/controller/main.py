from discord.ext import commands
from dotenv import load_dotenv
from Bot.utils.role_manager import roles
from Bot.config.config import Config
import discord, os

load_dotenv()

intents = discord.Intents.all()

Bot = commands.Bot(command_prefix="t!", intents=intents)

@Bot.event
async def on_ready():
    for files in os.listdir(os.path.join(os.getcwd(), "Bot", "cogs")):
        if files.endswith(".py"):
            try:
                await Bot.load_extensions(f"Bot.cogs.{files[:-3]}")
            except:
                pass
    roles(Bot, Config.server_name)


    
        

    




