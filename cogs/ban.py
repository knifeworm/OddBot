import discord
from discord.ext import commands
from datetime import datetime
today = datetime.today()
class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member = None, *, reason = None):
        if member == None:
            embed = discord.Embed(title="Banned Member", color=0xFF0000)
            embed.add_field(name="Member Banned", value=f"{member.name}#{member.discriminator}", inline=False)
            embed.add_field(name="Reason", value=f"{reason}", inline=False)
            embed.add_field(name="Time", value=today, inline=False)
            await ctx.send(emebd=embed)
            memberEmbed = discord.Embed(title="You have been banned.", description=f"Guild: {ctx.guild.name}", color=0xFF0000)
            memberEmbed.add_field(name="Staff Member", value=f"{ctx.author.name}#{ctx.author.discriminator}", inline=False)
            memberEmbed.add_field(name="Reason", value=f"{reason}", inline=False)
            memberEmbed.add_field(name="Time", value=today, inline=False)
            try:
                await member.send(embed=memberEmbed)
                await member.ban(reason=reason)
            except discord.DiscordException:
                await ctx.send("Member has not been informed that they have been banned. Due to there dms being closed.")
                await member.ban(reason=reason)
        else:
            await ctx.send('Please enter a member. e.g: !ban @OddBot reason')

def setup(bot):
    bot.add_cog(ban(bot))