import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from player import *
from bingocard import *

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Publix bot just clocked in")

@bot.command()
async def playbingo(ctx):
    card = BingoCard()
    player = Player(ctx.author.display_name, card)
    await ctx.send(f"{ctx.author.mention} started playing Publix Bingo!")
    player.print()

bot.run(TOKEN)