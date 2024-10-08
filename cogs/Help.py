import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Help.py is ready")
    
    @commands.command()
    async def commands(self, ctx): 
        await ctx.send("**Commands:**\n"
                       "- !ping: return pong\n"
                       "- !HB @someone: for giving a HB\n"
                       "- !etfs: view the current stats\n"
                       "- !cryptos: view the current stats\n"
                       "- !actions: view the current stats")

async def setup(client):
    await client.add_cog(Help(client))
