import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-hello'):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            print(f'{member} has joined the server')
            await member.create_dm()
            await member.dm_channel.send(f'Hi {member.name}, welcome to the server!', delete_after = 50)
            await channel.send(f'Hi {member.mention}, yang betah di server ya!')

@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            print(f'{member} has left the server')
            await channel.send(f'Bye bye {member.mention}!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong {round(client.latency*1000)}ms')

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain',
                 'It is decidedly so',
                 'Without a doubt',
                 'Yes – definitely',
                 'You may rely on it',
                 'As I see it, yes',
                 'Most likely',
                 'Outlook good',
                 'Yes',
                 'Signs point to yes',
                 'Reply hazy, try again',
                 'Ask again later',
                 'Better not tell you now',
                 'Cannot predict now',
                 'Concentrate and ask again',
                 "Don't count on it",
                 'My reply is no',
                 'My sources say no',
                 'Outlook not so good',
                 'Very doubtful']
    await ctx.send(f'Question : {question}\nAnswer : {random.choice(responses)}')

client.run('NzE2MDgzOTY2NjM3MjQ0NTE2.XucS1A.oQhgb6f3D2Y8essxtH3jxLHhB-Y')