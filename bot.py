import discord
from discord.ext import commands
import config
import os

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online")



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print("Cogs loaded")
    else:
        print("One cog failed to load.")

bot.run(config.token)