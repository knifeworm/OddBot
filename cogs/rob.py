import discord
from discord.ext import commands
import logging
import os
import json
import random
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

async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
    return bal


class rob(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rob(self, ctx, member : discord.Member=None):
        if member == None:
            await ctx.send("Please mention someone to rob.")
            return
        
        await open_account(member)
        
        bal = await update_bank(member)

        if bal[0]<100:
            await ctx.send("It's not worth it!")
            return

        earnings = random.randrange(0, bal[0])

        await update_bank(ctx.author,earnings,"wallet")
        await update_bank(member,-1*earnings,"wallet")

        await ctx.send(f"You robbed {earnings} coins from {member.mention}")
        await member.send(f"You have been robbed by {ctx.author.mention} in {ctx.guild.name}!")

def setup(bot):
    bot.add_cog(rob(bot))