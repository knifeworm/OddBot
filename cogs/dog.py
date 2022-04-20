import discord
from discord.ext import commands
import logging
import aiohttp

logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class dog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()
            embed = discord.Embed(title="Doggo!", description="Here have a cute doggo.", color=0x00FF00)
            embed.set_image(url=dogjson['link'])
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(dog(bot))