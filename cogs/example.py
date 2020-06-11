import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #event
    @commands.Cog.listener()
    async def on_ready(self):
        pass

    #commands
    @commands.command()
    async def test_ping(self,ctx):
        await ctx.send(f'Pong!')

def setup(client):
    client.add_cog(Example(client))


