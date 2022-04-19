import discord
from discord.ext import commands
import logging
import os
import json
logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def create_automod(guild):
    
    with open("automod.json", "r") as f:
        data = json.load(f)

    if str(guild.id) in data:
        return False
    else:
        data[str(guild.id)] = {}
        data[str(guild.id)]["auto"] = "yes"

        with open("automod.json", "w") as f:
            json.dump(data,f)


class automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def automod(self, ctx, option : str):
        await create_automod(ctx.guild)
        
        with open("automod.json", "r") as f:
            data = json.load(f)

        if option == "off":
            stuff2 = data[str(ctx.guild.id)]["auto"]
            if stuff2 == "yes":
                await ctx.send("Auto mod turned off.")
                data[str(ctx.guild.id)]["auto"] = "no"
                with open("automod.json","w") as f:
                    json.dump(data,f)
            elif stuff2 == "no":
                await ctx.send("Automod is already turned off.")
        elif option == "on":
            stuff = data[str(ctx.guild.id)]["auto"]
            if stuff == "yes":
                await ctx.send("Auto mod is already on.")
            elif stuff == "no":
                await ctx.send("Auto mod turned on.")
                data[str(ctx.guild.id)]["auto"] = "yes"
                with open("automod.json","w") as f:
                    json.dump(data,f)


def setup(bot):
    bot.add_cog(automod(bot))