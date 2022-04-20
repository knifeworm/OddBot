import discord
from discord.ext import commands
import logging
import json

logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class changeprefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(administrator = True)
    async def changeprefix(self, ctx, prefix : str):
        print("Yo!")
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        
        string = str(ctx.guild.id)
        prefixes[string] = prefix

        with open("prefixes.json","w") as f:
            json.dump(prefixes,f)
        
        await ctx.send(f"The prefix has been changed to {prefix}")


def setup(bot):
    bot.add_cog(changeprefix(bot))