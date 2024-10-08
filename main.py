import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv


load_dotenv()

# Make sure you have these variables
prefix = os.getenv("PREFIX")
token = os.getenv("TOKEN")

client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"{client.user} is ready")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await client.load_extension(f"cogs.{filename[:-3]}")
            except Exception as e:
                print(f"Something was wrong {filename}: {e}")

async def main():
    async with client:
        await load()
        await client.start(token)

asyncio.run(main())
