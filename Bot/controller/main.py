from discord.ext import commands
from dotenv import load_dotenv
from Bot.utils.role_manager import roles
from Bot.config.config import Config
from Bot.cogs.presence_manager import Presence
import discord, os

load_dotenv()

intents = discord.Intents.all()
bot_logger = Config.bot_logger
Bot = commands.Bot(command_prefix="t!", intents=intents)
roles(Bot, Config.server["Name"])
@Bot.event
async def on_ready():
    for files in os.listdir(os.path.join(os.getcwd(), "Bot", "cogs")):
        if files.endswith(".py"):
            try:
                await Bot.load_extension(f"Bot.cogs.{files[:-3]}")
                bot_logger.info(f"Bot loaded extensions {files}")
            except Exception as e:
                bot_logger.error(e)
    await Presence.change_presence.start()
                
    


    
        

    




