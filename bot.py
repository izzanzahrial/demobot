import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('bot is ready!!!')

client.run('NzE2MDgzOTY2NjM3MjQ0NTE2.XtQ6JQ.l9W6yiDW2_kkFvhVhI-Zipn0Maw')
