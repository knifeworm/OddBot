import discord
from discord.ext import commands
import logging
import os
import config

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot.remove_command('help')

logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

@bot.event
async def on_ready():
    logging.info('Bot is online!')
    print("Bot is online!")



@bot.command()
async def load(ctx, extension):
    if ctx.author.id == 866285734808780812:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f"Loaded {extension}")
    else:
        await ctx.send("Only the owner of the bot can run this command.")


@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == 866285734808780812:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f"Unloaded {extension}")
    else:
        await ctx.send("Only the owner of the bot can run this command.")


@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == 866285734808780812:
        bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f"Reloaded {extension}")
    else:
        await ctx.send("Only the owner of the bot can run this command.")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        logging.info(f'Loaded Cog: {filename[:-3]}')
        print(f"Loaded cog {filename[:-3]}")
    else:
        logging.warning(f'Failed to load cog: {filename[:-3]}')
        print(f"Failed to load cog. {filename[:-3]}")

bot.run(config.token)