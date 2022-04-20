import discord
from discord.ext import commands
import logging
import os
import config
import json
import asyncio
import random
import datetime
import json
from discord.ext.commands import CommandNotFound

intents = discord.Intents.default()
intents.members = True

def get_prefix(bot,message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix=get_prefix, intents=intents)

fitered_words = ["fuck", "f u c k", "shit", "s h i t", "f.u.c.k", "s.h.i.t" "f. u. c. k" "f .u .c .k", "s. h. i. t", "s .h .i .t", "nigga" "n.i.g.g.a" "NIGGA", "N I G G A", "N.I.G.G.A", "n i g g a", "bitch", "BITCH", "B.I.T.C.H", "b.i.t.c.h", "b i c h", "B I C H", "cock", "COCK", "C.O.C.K", "C.0.C.K", "c.o.c.k", "c.0.c.k", "c o c k", "c 0 c k", "C O C K", "C 0 C K"]

bot.remove_command('help')

logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

@bot.event
async def on_ready():
    logging.info('Bot is online!')
    print("Bot is online!")
    #print("Credits to buzE for helping me with 1 line of code.")


@bot.event
async def on_guild_join(guild):
    with open("automod.json", 'r') as f:
        data = json.load(f)
    
    data[str(guild.id)]["auto"] = {}
    data[str(guild.id)]["auto"] = "yes"

    with open("automod.json", "w") as f:
        json.dump(data,f)

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "-"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f"The command {error} you have executed is not found. use the command !help for a list of available commands")


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


@bot.event
async def on_message(msg):
    with open("automod.json",'r') as f:
        data = json.load(f)
    
    auto = data[str(msg.guild.id)]["auto"]
    if(auto == "yes"):
        for word in fitered_words:
            if word in msg.content:
                await msg.delete()
                await msg.channel.send("Please don't swear")
    await bot.process_commands(msg)

@bot.event
async def on_message(msg):
    try:
        if msg.mentions[0] == bot.user:
            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)
        
            pre = prefixes[str(msg.guild.id)]
            await msg.channel.send(f"My prefix for this server is {pre}")
    except:
        pass
    await bot.process_commands(msg)

bot.run(config.token)