import discord
from discord.ext import commands

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        embed = discord.Embed(title="Ping 🏓", description="Shows bots latency")
        embed.add_field(name='Ping', value = f"{round(self.bot.latency * 1000)}ms")

        await ctx.send(embed=embed)

    @commands.command(aliases=['botinfo'])
    @commands.guild_only()
    async def aboutbot(self,ctx):
        embed = discord.Embed(title="Botname",color=ctx.author.colour, timestamp=ctx.message.created_at)

        embed.add_field(name = "```Bot Version```", value="1.0.0")
        embed.add_field(name = "```Total Servers```", value=f"{len(self.bot.guilds):,} Servers")
        embed.add_field(name="```Users```", value=f"{len(self.bot.users):,}")
        embed.add_field(name = "```Bot developer```", value="<@671390595184459782> <@959276033683628122> <@952560202635427841>``@{Ansh}#0607 Blacky#9125 AkAbhijit#7178``")
        embed.add_field(name = "```Support Server```", value="[CLICK ME](https://discord.gg/coders)")
        embed.add_field(name = "```Invite```", value="[CLICK ME](invitelinkhere)")
        embed.add_field(name="Github repository", value="[CLICK ME](https://github.com/Coders-src/discord.py-handler)")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Information(bot))