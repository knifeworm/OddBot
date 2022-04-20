import discord
from discord.ext import commands
import logging

logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help", color=0x00ff00)
        embed.add_field(name="!serverinfo", value="Displays information about the server you ran the command in.", inline=False)
        embed.add_field(name="!userinfo", value="Displays information about you or the person you mention.", inline=False)
        embed.add_field(name="!help", value="Displays the bots help.", inline=False)
        embed.add_field(name="!clear", value="**MODERATION COMMAND** Clears the amount of messages you input.", inline=False)
        embed.add_field(name="!help", value="Displays this embed!", inline=False)
        embed.add_field(name="!ban", value="**MODERATION COMMAND** Bans the member you specifiy.", inline=False)
        embed.add_field(name="!balance, !bal", value="Shows your wallet and bank balance.", inline=False)
        embed.add_field(name="!beg", value="Beg for money peasent.", inline=False)
        embed.add_field(name="!deposit", value="Deposit money into your bank.", inline=False)
        embed.add_field(name="!pay", value="Pays another member money.", inline=False)
        embed.add_field(name="!kick", value="**MODERATION COMMAND** Kicks the member you specifiy.", inline=False)
        embed.add_field(name="!automod", value="**MODERATION COMMAND** Allows you to enable or disable automod.", inline=False)
        embed.add_field(name="!withdraw", value="Lets you withdraw money from your bank.", inline=False)
        await ctx.send(embed=embed)
        if ctx.guild.owner.name == ctx.author.name:
            logging.info(f"The owner of {ctx.guild.name} has ran the help command.")
            print(f"The owner of {ctx.guild.name} has ran the help command.")
        else:  
            logging.info(f"{ctx.author.name} has run the help command in {ctx.guild.name} with the id of {ctx.guild.id}")
            print(f"{ctx.author.name} has ran the help command in {ctx.guild.name} with the id of {ctx.guild.id}")

def setup(bot):
    bot.add_cog(help(bot))