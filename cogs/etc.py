import discord
import random
from discord.ext import commands

class Etc(commands.Cog):

    def __init__(self, client):
        self.client = client

    #event
    @commands.Cog.listener()
    async def test(self):
        pass

    #command
    @commands.command()
    async def test(self,ctx):
       pass

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
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

def setup(client):
    client.add_cog(Etc(client))
