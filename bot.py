from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import playerInfo
import clanInfo


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
    await ctx.send(playerInfo.printName('data.json'))

@bot.command()
async def tag(ctx):
    await ctx.send(playerInfo.printTag('data.json'))

@bot.command()
async def PlayerInfo(ctx, player_tag: str):
    filename = f"data_{player_tag}.json"
    player_info = playerInfo.PlayerInfo(player_tag, filename)

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

@bot.command()
async def ClanInfo(ctx, clan_tag: str):
    filename = f"data{clan_tag}.json"
    clan_info = clanInfo.clanInfo(clan_tag, filename)

    try:
        clan_info.getClanData()
        tag = clan_info.getTag()
        name = clan_info.getName()

        await ctx.send(f'Clan Tag: {tag} \nClan Name: {name}')
    except Exception as e:
        await ctx.send(f'An error occured: {str(e)}')
    finally:
        clan_info.deleteFile()

bot.run(os.getenv('DISCORD_API_KEY'))