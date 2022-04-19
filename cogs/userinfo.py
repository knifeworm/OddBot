from sqlite3 import adapt
import discord
from discord.ext import commands
import logging

logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, member : discord.Member = None):
        if member == None:
            embed = discord.Embed(title="User Information", color=0x00ff00)
            embed.add_field(name="Username", value=f"{ctx.author.name}", inline=False)
            embed.add_field(name="UserID", value=f"{ctx.author.id}", inline=False)
            isowner = False
            if(ctx.guild.owner.name == ctx.author.name):
                isowner = True
            else:
                isowner = False
            embed.add_field(name="Is Owner?", value=isowner, inline=False)
            embed.add_field(name="Creation Date", value=f"{ctx.author.created_at}", inline=False)
            embed.add_field(name="Joined Date", value=f"{ctx.author.joined_at}", inline=False)
            await ctx.send(embed=embed)
            if ctx.guild.owner.name == ctx.author.name:
                logging.info(f"The owner of {ctx.guild.name} has ran the userinfo command.")
                print(f"The owner of {ctx.guild.name} has ran the userinfo command.")
            else:  
                logging.info(f"{ctx.author.name} has run the userinfo command in {ctx.guild.name} with the id of {ctx.guild.id}")
                print(f"{ctx.author.name} has ran the userinfo command in {ctx.guild.name} with the id of {ctx.guild.id}")
        else:
            embed = discord.Embed(title="User Information", color=0x00ff00)
            embed.add_field(name="Username", value=f"{member.name}", inline=False)
            embed.add_field(name="UserID", value=f"{member.id}", inline=False)
            isowner = False
            if(ctx.guild.owner.name == member.name):
                isowner = True
            else:
                isowner = False
            embed.add_field(name="Is Owner?", value=isowner, inline=False)
            embed.add_field(name="Creation Date", value=f"{member.created_at}", inline=False)
            embed.add_field(name="Joined Date", value=f"{member.joined_at}", inline=False)
            await ctx.send(embed=embed)
            if ctx.guild.owner.name == ctx.author.name:
                logging.info(f"The owner of {ctx.guild.name} has ran the userinfo command.")
                print(f"The owner of {ctx.guild.name} has ran the userinfo command.")
            else:  
                logging.info(f"{ctx.author.name} has run the userinfo command in {ctx.guild.name} with the id of {ctx.guild.id}")
                print(f"{ctx.author.name} has ran the userinfo command in {ctx.guild.name} with the id of {ctx.guild.id}")

def setup(bot):
    bot.add_cog(userinfo(bot))