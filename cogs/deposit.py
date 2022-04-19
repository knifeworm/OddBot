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


class deposit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def deposit(self, ctx, amount : int):
        users = await get_bank_data()

        bal = users[str(ctx.author.id)]["wallet"]

        if(bal < amount):
            await ctx.send("The number you entered you don't have in ur wallet.")
        else:
            users[str(ctx.author.id)]["bank"] += amount
            users[str(ctx.author.id)]["wallet"] -= amount
            with open("mainbank.json", "w") as f:
                json.dump(users,f)
            await ctx.send(f"Deposited {amount} of coins to your bank.")
    
    @deposit.error
    async def deposit_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Please enter the amount you want to deposit.")

def setup(bot):
    bot.add_cog(deposit(bot))