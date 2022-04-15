import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online")


bot.run(config.token)