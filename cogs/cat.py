import discord
from discord.ext import commands
import logging
import aiohttp

logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class cat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            catjson = await request.json()
            embed = discord.Embed(title="Cat!", description="Here have a cute cat.", color=0x00FF00)
            embed.set_image(url=catjson['link'])
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(cat(bot))