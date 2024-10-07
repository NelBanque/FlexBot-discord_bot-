import discord
from discord.ext import commands
import yfinance as yf
import matplotlib.pyplot as plt
import io

class CryptosView(discord.ui.View):
    @discord.ui.button(label="Bitcoin", style=discord.ButtonStyle.primary)
    async def bitcoin_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        crypto = yf.Ticker('BTC-USD')  # Bitcoin
        price = crypto.history(period='1d')['Close'].iloc[-1]
        history = crypto.history(period='1y')

        await interaction.response.send_message(f"{interaction.user.mention}, the current price of Bitcoin is €{price:.2f}")

        # Create a graph of the Bitcoin price history
        fig, ax = plt.subplots()
        ax.plot(history.index, history['Close'], label='Close Price', color='orange')
        ax.set(xlabel='Date', ylabel='Price (EUR)', title='Bitcoin Price History (EUR)')
        ax.grid()
        ax.legend()

        # Save the graph to a bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Send the graph as an attachment
        await interaction.channel.send(file=discord.File(fp=buf, filename='bitcoin_price_history.png'))
        plt.close(fig)

    @discord.ui.button(label="Ethereum", style=discord.ButtonStyle.primary)
    async def ethereum_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        crypto = yf.Ticker('ETH-USD')  # Ethereum
        price = crypto.history(period='1d')['Close'].iloc[-1]
        history = crypto.history(period='1y')

        await interaction.response.send_message(f"{interaction.user.mention}, the current price of Ethereum is €{price:.2f}")

        # Create a graph of the Ethereum price history
        fig, ax = plt.subplots()
        ax.plot(history.index, history['Close'], label='Close Price', color='blue')
        ax.set(xlabel='Date', ylabel='Price (EUR)', title='Ethereum Price History (EUR)')
        ax.grid()
        ax.legend()

        # Save the graph to a bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Send the graph as an attachment
        await interaction.channel.send(file=discord.File(fp=buf, filename='ethereum_price_history.png'))
        plt.close(fig)

    @discord.ui.button(label="Tether", style=discord.ButtonStyle.primary)
    async def tether_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        crypto = yf.Ticker('USDT-USD')  # Tether
        price = crypto.history(period='1d')['Close'].iloc[-1]
        history = crypto.history(period='1y')

        await interaction.response.send_message(f"{interaction.user.mention}, the current price of Tether is €{price:.2f}")

        # Create a graph of the Tether price history
        fig, ax = plt.subplots()
        ax.plot(history.index, history['Close'], label='Close Price', color='green')
        ax.set(xlabel='Date', ylabel='Price (EUR)', title='Tether Price History (EUR)')
        ax.grid()
        ax.legend()

        # Save the graph to a bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Send the graph as an attachment
        await interaction.channel.send(file=discord.File(fp=buf, filename='tether_price_history.png'))
        plt.close(fig)

class CryptosCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('CryptosCog is ready')

    @commands.command()
    async def cryptos(self, ctx):
        view = CryptosView()
        await ctx.send(f"{ctx.author.mention}, select a cryptocurrency:", view=view)

async def setup(bot):
    await bot.add_cog(CryptosCog(bot))
