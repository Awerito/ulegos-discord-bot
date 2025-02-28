import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
# Scripts
from scripts_requests.github_request import *
from scripts_requests.wikipedia_request import *
from scripts_requests.youtube_request import *
from scripts_requests.reddit_request import *
from scripts_requests.schedule_request import *


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


@bot.command(aliases=['youtube', 'yt'])
async def _youtube(ctx, *, search):
    result = youtube_request(search)
    await ctx.send(result)


@bot.command(aliases=['reddit', 'rd'])
async def _reddit(ctx, *, search):
    result = reddit_request(search)
    await ctx.send(result)


@bot.command(aliases=['ulegos', 'ula'])
async def _ulegos(ctx, *, search):
    result = schedule_request(search)
    if result == "Success":
        await ctx.send(file=discord.File('out.jpeg'))
    else:
        await ctx.send(result)


load_dotenv()
secret_key = os.getenv('DISCORD_TOKEN')
bot.run(secret_key)
