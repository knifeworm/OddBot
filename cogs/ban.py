import discord
from discord.ext import commands
import logging
from datetime import date, datetime
today = datetime.today()
logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(title="Successfully Banned", color=0x00FF00)
        embed.add_field(name="Member Banned", value=f"{member.mention}", inline=False)
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        embed.add_field(name="Date", value=today, inline=False)
        await ctx.send(embed=embed)
        memberEmbed = discord.Embed(title="You have been banned!", description=f"Guild: {ctx.guild.name}", color=0xFF0000)
        memberEmbed.add_field(name="Staff Member", value=f"{ctx.author.mention}", inline=False)
        memberEmbed.add_field(name="Reason", value=f"{reason}", inline=False)
        memberEmbed.add_field(name="Date", value=today, inline=False)
        if ctx.guild.owner.name == ctx.author.name:
            logging.info(f"The owner of {ctx.guild.name} has ran the ban command.")
            print(f"The owner of {ctx.guild.name} has ran the ban command.")
        else:  
            logging.info(f"{ctx.author.name} has run the ban command in {ctx.guild.name} with the id of {ctx.guild.id}")
            print(f"{ctx.author.name} has ran the ban command in {ctx.guild.name} with the id of {ctx.guild.id}")
        try:
            await member.send(embed=memberEmbed)
            await member.ban(reason=reason)
        except commands.NoPrivateMessage:
            await ctx.send(f"Unable to send a message to {member.mention} still have been banned.")
            await member.ban(reason=reason)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("ERROR: Please enter a member. E.G: !ban @OddBot swearing")

def setup(bot):
    bot.add_cog(ban(bot))