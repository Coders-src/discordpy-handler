from click import command
import discord
from discord.ext import commands

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.guild_only()
    async def changeprefix(self, ctx, prefix=None):
        if prefix is None:
            return await ctx.send("Put in a prefix for me to change!")
        data = await self.bot.prefixes.find(ctx.guild.id)
        if data is None or "prefix" not in data:
            data = {"_id": ctx.guild.id, "prefix": prefix}
        data["prefix"] = prefix
        await self.bot.prefixes.upsert(data)
        await ctx.send("I have changed the server's prefix to {}".format(prefix))

    @commands.command(aliases=['dp'])
    @commands.has_permissions(manage_guild=True)
    @commands.guild_only()
    async def deleteprefix(self, ctx):
        await self.bot.prefixes.unset({"_id": ctx.guild.id , "prefix": 1})
        await ctx.send("The server's prefix has been set to default.")

def setup(bot):
    bot.add_cog(Config(bot))