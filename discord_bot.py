import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


bot = commands.Bot(command_prefix='./')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

load_dotenv()
secret_key = os.getenv('DISCORD_TOKEN')
bot.run(secret_key)
