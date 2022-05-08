#importing modules
import discord
from discord.ext import commands
import os
from webserver import keep_alive
from flask import Flask
from threading import Thread
import discordmongo
import sqlite3
import motor.motor_asyncio
import asyncio

#making flask server
app = Flask('')

@app.route('/')
def main():
    return 'Your bot in online! 🟢'

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    server = Thread(target=run)
    server.start()

# Function to get prefix
async def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or(bot.DEFAULT_PREFIX)(bot, message)

    try:
        data = await bot.prefixes.find(message.guild.id)

        if not data or "prefix" not in data:
            return commands.when_mentioned_or(bot.DEFAULT_PREFIX)(bot, message)
        return commands.when_mentioned_or(data["prefix"])(bot, message)
    except:
        return commands.when_mentioned_or(bot.DEFAULT_PREFIX)(bot, message)

# defining bot and intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=get_prefix, owner_id = 'Your id', intents = discord.Intents.all())
bot.remove_command('help')
bot.DEFAULT_PREFIX = 'a!'

#function for status
async def status():
    while True:
        await bot.wait_until_ready()
        await bot.change_presence(activity=discord.Game(name = f"{len(bot.guilds):,} Servers|a!help"))
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Game(name = f"{len(bot.users):,} Users|a!help"))
        await asyncio.sleep(20)

#making bot ready function
@bot.event
async def on_ready():
    print("Your bot is ready.")
    bot.loop.create_task(status())

# accessing files from cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"cogs - {filename[:-3]} ")

#connection to mongo
if __name__ == '__main__':
    bot.mongo = motor.motor_asyncio.AsyncIOMotorClient("MONGO_URL")
    bot.db = bot.mongo["discord"]
    bot.prefixes = discordmongo.Mongo(connection_url = bot.db, dbname='prefixes')

#accessing the whole directory
os.chdir(r'./')


#makeing bot online
keep_alive()
bot.run("TOKEN")
