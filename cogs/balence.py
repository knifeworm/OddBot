import discord
from discord.ext import commands
import logging
import os
import json
logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json","w") as f:
        json.dump(users,f)
        logging.info(f"Just created a new account for {user.name}")
    return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)
    
    return users

class balence(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=["bal", "balance"])
    async def balence(self, ctx, member : discord.Member = None):
        if member == None:
            await open_account(ctx.author)

            users = await get_bank_data()

            wallet_amount = users[str(ctx.author.id)]["wallet"]
            bank_amount = users[str(ctx.author.id)]["bank"]

            embed = discord.Embed(title=f"{ctx.author.name}'s balance", color=0x00FF00)
            embed.add_field(name="Wallet balance", value=wallet_amount)
            embed.add_field(name="Bank balance", value=bank_amount)
            await ctx.send(embed=embed)
        else:
            await open_account(member)

            users = await get_bank_data()


            wallet_amount = users[str(member.id)]["wallet"]
            bank_amount = users[str(member.id)]["bank"]

            embed = discord.Embed(title=f"{member.name}'s balance", color=0x00FF00)
            embed.add_field(name="Wallet balance", value=wallet_amount)
            embed.add_field(name="Bank balance", value=bank_amount)
            await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(balence(bot))