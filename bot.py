import discord
from discord.ext import commands

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

bot.run('MTI4OTk0OTc4MzEwNDAzMjg2OA.GawliT.9YgKfOGGQK_U4Ib6X8NEbLZybJg4gkbN5fLm-c')