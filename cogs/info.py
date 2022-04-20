import discord
from discord.ext import commands
import logging
import time
import os
import sys
import psutil
import platform

import shutil

total, used, free = shutil.disk_usage("/")
l1, l2, l3 = psutil.getloadavg()
CPU_use = (l3/os.cpu_count()) * 100
logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def get_ram_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="Bot Information", color=0x00FF00)
        embed.add_field(name="Bot Name", value="OddBot", inline=False)
        embed.add_field(name="Server Count", value=f"{str(len(self.bot.guilds))} servers!", inline=False)
        embed.add_field(name="CPU Usage", value=f"{CPU_use}%", inline=False)
        embed.add_field(name="RAM Usage", value=f"{int(get_ram_usage() / 1024 / 1024)}MB", inline=False)
        embed.add_field(name="OS Name", value=f"{platform.system()}", inline=False)
        embed.add_field(name="Total Disk Space", value=f"{total // (2**30)}GB", inline=False)
        embed.add_field(name="Used Disk Space", value=f"{used // (2**30)}GB", inline=False)
        embed.add_field(name="Free Disk Space", value=f"{free // (2**30)}GB", inline=False)
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1
        embed.add_field(name="Number of Members", value=f"{members}", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))