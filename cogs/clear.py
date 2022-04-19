import discord
from discord.ext import commands
import logging
import time
logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self, ctx, amount=None):
        if amount == None:
            await ctx.channel.purge(limit=10)
            msg = await ctx.send("Deleted 10 messages.")
            time.sleep(3)
            await msg.delete()
            if ctx.guild.owner.name == ctx.author.name:
                logging.info(f"The owner of {ctx.guild.name} has ran the clear command.")
                print(f"The owner of {ctx.guild.name} has ran the clear command.")
            else:  
                logging.info(f"{ctx.author.name} has run the clear command in {ctx.guild.name} with the id of {ctx.guild.id}")
                print(f"{ctx.author.name} has ran the clear command in {ctx.guild.name} with the id of {ctx.guild.id}")
        else:
            if amount > "100":
                await ctx.send("Please enter a number less than or equal to 100.")
                if ctx.guild.owner.name == ctx.author.name:
                    logging.info(f"The owner of {ctx.guild.name} has ran the clear command.")
                    print(f"The owner of {ctx.guild.name} has ran the clear command.")
                else:  
                    logging.info(f"{ctx.author.name} has run the clear command in {ctx.guild.name} with the id of {ctx.guild.id}")
                    print(f"{ctx.author.name} has ran the clear command in {ctx.guild.name} with the id of {ctx.guild.id}")
            else:
                await ctx.channel.purge(limit=int(amount))
                msg = await ctx.send(f"Deleted {amount} messages.")
                time.sleep(3)
                await msg.delete()
                if ctx.guild.owner.name == ctx.author.name:
                    logging.info(f"The owner of {ctx.guild.name} has ran the clear command.")
                    print(f"The owner of {ctx.guild.name} has ran the clear command.")
                else:  
                    logging.info(f"{ctx.author.name} has run the clear command in {ctx.guild.name} with the id of {ctx.guild.id}")
                    print(f"{ctx.author.name} has ran the clear command in {ctx.guild.name} with the id of {ctx.guild.id}")
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Bad Argument error.")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Missing permissions.")

def setup(bot):
    bot.add_cog(clear(bot))