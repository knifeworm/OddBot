import discord
from discord.ext import commands
import logging
from datetime import date, datetime
today = datetime.today()
logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class kick(commands.Cog):
    def _init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(title="Successfully Kicked", color=0x00ff00)
        embed.add_field(name="Member Kicked", value=f"{member.mention}", inline=False)
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        embed.add_field(name="Date", value=today, inline=False)
        await ctx.send(embed=embed)
        memberEmbed = discord.Embed(title="You have been kicked!", description=f"Guild: {ctx.guild.name}", color=0xFF0000)
        memberEmbed.add_field(name="Staff Member", value=f"{ctx.author.mention}", inline=False)
        memberEmbed.add_field(name="Reason", value=f"{reason}", inline=False)
        memberEmbed.add_field(name="Date", value=today, inline=False)
        if ctx.guild.owner.name == ctx.author.name:
            logging.info(f"The owner of {ctx.guild.name} has ran the kick command.")
            print(f"The owner of {ctx.guild.name} has ran the kick command.")
        else:  
            logging.info(f"{ctx.author.name} has run the kick command in {ctx.guild.name} with the id of {ctx.guild.id}")
            print(f"{ctx.author.name} has ran the kick command in {ctx.guild.name} with the id of {ctx.guild.id}")
        try:
            await member.send(embed=memberEmbed)
            await member.kick()
        except commands.NoPrivateMessage:
            await ctx.send(f"Unable to send a message to {member.mention} still have been kicked.")
            await member.kick()

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"ERROR! Please enter a member. E.G: !kick @OddBot swearing")


def setup(bot):
    bot.add_cog(kick(bot))