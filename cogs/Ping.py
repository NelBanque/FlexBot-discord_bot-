import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping.py is ready")
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")


async def setup(client):
    await client.add_cog(Ping(client))
