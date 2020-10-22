import discord
from discord.ext import commands
import os
from os.path import join, dirname
from dotenv import load_dotenv


bot = commands.Bot(command_prefix='./')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# Accessing variables.
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
secret_key = os.getenv('DISCORD_TOKEN')
bot.run(secret_key)
