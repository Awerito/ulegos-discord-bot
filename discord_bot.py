import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
# Custom
from scripts_requests.github_request import *
from scripts_requests.wikipedia_request import *


bot = commands.Bot(command_prefix='./')


@bot.event
async def on_ready():
    print("Bot ready!")


@bot.command(aliases=['github', 'git', 'g'])
async def _github(ctx, *, search):
    result = github_request(search)
    await ctx.send(result)


@bot.command(aliases=['wikipedia', 'wiki', 'w'])
async def _wikipedia(ctx, *, search):
    result = wikipedia_request(search)
    await ctx.send(result)


load_dotenv()
secret_key = os.getenv('DISCORD_TOKEN')
bot.run(secret_key)
