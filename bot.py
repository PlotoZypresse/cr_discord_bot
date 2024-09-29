from dotenv import load_dotenv
import os
import discord
from discord.ext import commands


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Event that triggers when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# A simple command to test the bot
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(os.getenv('DISCORD_API_KEY'))