import discord
from discord.ext import commands

class Birthday(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Birthday.py is ready")
    
    @commands.command(name="HB")
    async def hb(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("You need to tag someone to wish them a happy birthday!")
        else:
            await ctx.send(f"Happy Birthday, 🎉 {member.mention} 🎉")

async def setup(client):
    await client.add_cog(Birthday(client))
