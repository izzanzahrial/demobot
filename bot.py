import discord
import os
import youtube_dl
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get

client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Activity(type=discord.ActivityType.listening, name='-help'))
    print('We have logged in as {0.user}'.format(client))

@tasks.loop(seconds=5)
async def loop_status():
    pass #https://www.youtube.com/watch?v=RK8RzuUMYt8&list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ&index=9

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
    await ctx.send(f'Pong {round(client.latency * 1000)}ms')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit=amount+1)

def is_it_me(ctx):
    return ctx.author.id == 327723419443658753

@client.command()
@commands.check(is_it_me)
async def onlyme(ctx):
    await ctx.send(f'Only you {ctx.author.mention} no one can')

@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



@client.command(aliases=['j'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel}")

@client.command(aliases=['L','l'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f'Bot has left the {channel}')
        await ctx.send(f'Bot left the {channel}')
    else:
        print(f"Bot wans't not in the {channel}")
        await ctx.send(f"I'am not in the {channel}")

@client.command(aliases=['p'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("The song has been removed")
    except PermissionError:
        print("Can't remove song, cause being played")
        await ctx.send("ERROR: Music is playing")
        return

    await ctx.send("Getting ready")

    voice = get(client.voice_clients,guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessor' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading song now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")

client.run(YOUR_TOKEN)