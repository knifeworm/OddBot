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



class withdraw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def withdraw(self, ctx, amount : int):
        users = await get_bank_data()

        bal = users[str(ctx.author.id)]["bank"]

        if(bal < amount):
            await ctx.send("The number you entered you don't have in ur bank.")
        else:
            users[str(ctx.author.id)]["wallet"] += amount
            users[str(ctx.author.id)]["bank"] -= amount
            with open("mainbank.json", "w") as f:
                json.dump(users,f)
            await ctx.send(f"Withdrawed {amount} of coins to your wallet.")

    @withdraw.error
    async def withdraw_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter a amount to withdraw.")

def setup(bot):
    bot.add_cog(withdraw(bot))