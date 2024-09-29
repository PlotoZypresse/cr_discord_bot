from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import cr_api


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# name = cr_api.printName('data.json')
# tag = cr_api.printTag('data.json')

# print(name)
# Event that triggers when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# A simple command to test the bot
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def name(ctx):
    await ctx.send(cr_api.printName('data.json'))

@bot.command()
async def tag(ctx):
    await ctx.send(cr_api.printTag('data.json'))

@bot.command()
async def getPlayerInfo(ctx, player_tag: str):
    filename = f"data_{player_tag}.json"
    player_info = cr_api.PlayerInfo(player_tag, filename)

    try:
        player_info.getPlayerData()
        tag = player_info.getTag()
        name = player_info.getName()
        winRate = player_info.playerWinRate()
        clan = player_info.clanInfo()
        await ctx.send(f'Player Tag: {tag} \nPlayer Name: {name} \n{winRate} \nPlayer Clan: {clan}')
    except Exception as e:
        await ctx.send(f'An error occurred: {str(e)}')
    finally:
        player_info.deleteFile()

bot.run(os.getenv('DISCORD_API_KEY'))