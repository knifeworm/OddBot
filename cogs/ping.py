import discord
from discord.ext import commands
import logging

logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {self.bot.latency * 1000:.2f}ms")
        if ctx.guild.owner.name == ctx.author.name:
            logging.info(f"The owner of {ctx.guild.name} has ran the ping command.")
            print(f"The owner of {ctx.guild.name} has ran the ping command.")
        else:  
            logging.info(f"{ctx.author.name} has run the ping command in {ctx.guild.name} with the id of {ctx.guild.id}")
            print(f"{ctx.author.name} has ran the ping command in {ctx.guild.name} with the id of {ctx.guild.id}")

def setup(bot):
    bot.add_cog(ping(bot))