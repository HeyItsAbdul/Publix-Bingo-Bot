import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


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
    b1 = BingoCard('Daniel')
    print(b1.bingoCard)
    await ctx.send(f"{ctx.author.mention} started playing Publix Bingo!")

bot.run(TOKEN)