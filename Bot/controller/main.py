from discord.ext import commands
from dotenv import load_dotenv
import discord, os

load_dotenv()

intents = discord.Intents.all()

Bot = commands.Bot(command_prefix="t!", intents=intents)

@Bot.event





