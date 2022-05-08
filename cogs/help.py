import discord
from discord.ext import commands


class HelpCog(commands.Cog, name='Help'):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    @commands.guild_only()
    async def help(self, ctx):
        embed = discord.Embed(title = "Help", description="Here is the list of all commands.")
        embed.add_field(name="Config", value="`changeprefix <newprefix>`, `deleteprefix`", inline=True)
        embed.add_field(name='Information', value="`help`, `ping`, `botinfo`", inline=True)
        embed.add_field(name='Owner', value='`load <cogname>`, `unload <cogname>`', inline=True)
        embed.add_field(name="Github repository", value="[CLICK ME](https://github.com/Coders-src/discord.py-handler)")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(HelpCog(bot))