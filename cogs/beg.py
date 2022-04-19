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


class beg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def beg(self, ctx):
        await open_account(ctx.author)

        users = await get_bank_data()


        earnings = random.randrange(101)

        await ctx.send(f"Someone gave you {earnings} coins!")

        users[str(ctx.author.id)]["wallet"] += earnings

        with open("mainbank.json","w") as f:
            json.dump(users,f)


def setup(bot):
    bot.add_cog(beg(bot))