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


class slots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def slots(self, ctx, amount = None):
        await open_account(ctx.author)

        if amount == None:
            await ctx.send("Please enter an amount.")
            return
        
        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[0]:
            await ctx.send("You don't have that much money.")
            return
        if amount<0:
            await ctx.send("Amount must be positive")
            return

        final = []
        for i in range(3):
            a = random.choice(["X", "0", "Q"])

            final.append(a)

        await ctx.send(str(final))

        if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
            await update_bank(ctx.author, -1*amount)
            await ctx.send("You won double the amount!")
        else:
            await update_bank(ctx.author,-1*amount)
            await ctx.send("You lost better luck next time.")

def setup(bot):
    bot.add_cog(slots(bot))