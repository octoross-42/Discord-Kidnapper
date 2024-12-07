import discord
from discord.ext import commands

import os
import sys
from collections import defaultdict

from setup.intents import getIntents
from setup.config import TOKEN

intents = getIntents()
bot = commands.Bot(command_prefix='!', intents=intents)

bot.planning = defaultdict(dict)
bot.kid = defaultdict(dict)
bot.serveurs = defaultdict(dict)

@bot.hybrid_command()
async def plan(context: commands.Context, arg1: int, arg2: str):
    print("id : ", context.guild.id)
    print("channel du serveur : ", bot.serveurs[context.guild.id])
    server = bot.serveurs[context.guild.id]
    if server:
    	if server["channel"]:
         	server["channel"].send("lalala")

@bot.hybrid_command()
async def reload(ctx):
    embed = discord.Embed(title='Reload', description=f'Bot is reloading', color=0xFFA500)
    await ctx.send(embed=embed)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    

@bot.hybrid_command()
async def set_channel(context: commands.Context, channel: str):
    for chan in context.guild.channels:
        if (chan.name == channel):
            bot.serveurs[context.guild.id]['channel'] = chan
            await context.send(f'Channel set to {channel}')
            print("id : ", context.guild.id)
            return
    await context.send(f'Channel not found')
 
@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')
	await bot.tree.sync()
	embed = discord.Embed(title='Bot is up', description=f'Bot has loaded', color=0xFFA500)
	for guild in bot.guilds:
		await guild.system_channel.send(embed=embed)

bot.run(TOKEN)