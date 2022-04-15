import discord
from discord.ext import commands
import config
import os

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online")


@bot.command()
async def load(ctx, extension):
    if ctx.author.id == config.owner_id:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f"Loaded Cog {extension}")
    else:
        await ctx.send("You are not the owner of this bot.")


@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == config.owner_id:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f"Unloaded Cog {extension}")
    else:
        await ctx.send("You are not the owner of this bot.")

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == config.owner_id:
        bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f"Reloaded Cog {extension}")
    else:
        await ctx.send("You are not the owner of this bot.")



for filename in os.listdir('./cogs/moderation'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.moderation.{filename[:-3]}')
        print("Moderation Cogs loaded")
    else:
        print("One cog failed to load.")

for filename in os.listdir('./cogs/info'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.info.{filename[:-3]}')
        print("Info Cogs loaded")
    else:
        print("One cog failed to load.")

for filename in os.listdir('./cogs/fun'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.fun.{filename[:-3]}')
        print("Fun Cogs loaded")
    else:
        print("One cog failed to load.")

bot.run(config.token)