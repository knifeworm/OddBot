import discord
from discord.ext import commands
import logging

logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        embed = discord.Embed(title="Server Information", description=f"Guild: {ctx.guild.name}", color=0x00ff00)
        embed.add_field(name="Guild Name", value=f"{ctx.guild.name}", inline=False)
        embed.add_field(name="Guild ID", value=f"{ctx.guild.id}", inline=False)
        total_text_channels = len(ctx.guild.text_channels)
        total_voice_channels = len(ctx.guild.voice_channels)
        total_channels = total_text_channels + total_voice_channels
        role_count = len(ctx.guild.roles)
        emoji_count = len(ctx.guild.emojis)
        online = 0
        for i in ctx.guild.members:
            if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
                online += 1
        embed.add_field(name="Text Channels", value=total_text_channels)
        embed.add_field(name="Voice Channels", value=total_voice_channels)
        embed.add_field(name="Total Channels", value=total_channels)
        embed.add_field(name="Verification Level", value=str(ctx.guild.verification_level))
        embed.add_field(name="Number Of Roles", value=role_count)
        embed.add_field(name="Number Of Emojis", value=emoji_count)
        embed.add_field(name="Currently Online", value=online)
        embed.add_field(name="Owner", value=f"{ctx.guild.owner.name}", inline=False)
        embed.add_field(name="Creation Date", value=f"{ctx.guild.created_at}")
        await ctx.send(embed=embed)
        if ctx.guild.owner.name == ctx.author.name:
            logging.info(f"The owner of {ctx.guild.name} has ran the serverinfo command.")
            print(f"The owner of {ctx.guild.name} has ran the serverinfo command.")
        else:  
            logging.info(f"{ctx.author.name} has run the serverinfo command in {ctx.guild.name} with the id of {ctx.guild.id}")
            print(f"{ctx.author.name} has ran the serverinfo command in {ctx.guild.name} with the id of {ctx.guild.id}")
        
def setup(bot):
    bot.add_cog(serverinfo(bot))