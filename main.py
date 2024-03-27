import discord
import os
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Streaming(name='CosmoS menu', url='https://saphireshop.xyz/'))
bot = Bot(token=os.environ.get('TOKEN'))

bot.run(bot)
