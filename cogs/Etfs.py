import discord
from discord.ext import commands
import yfinance as yf
import matplotlib.pyplot as plt
import io

class ETFsView(discord.ui.View):
    @discord.ui.button(label="S&P 500", style=discord.ButtonStyle.primary)
    async def sp500_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        etf = yf.Ticker('^GSPC')  # S&P 500
        price = etf.history(period='1d')['Close'].iloc[-1]
        history = etf.history(period='1y')

        await interaction.response.send_message(f"{interaction.user.mention}, the current price of S&P 500 is €{price:.2f}")

        # Create a graph of the S&P 500 price history
        fig, ax = plt.subplots()
        ax.plot(history.index, history['Close'], label='Close Price', color='blue')
        ax.set(xlabel='Date', ylabel='Price (EUR)', title='S&P 500 Price History (EUR)')
        ax.grid()
        ax.legend()

        # Save the graph to a bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Send the graph as an attachment
        await interaction.channel.send(file=discord.File(fp=buf, filename='sp500_price_history.png'))
        plt.close(fig)

    @discord.ui.button(label="Nasdaq 100", style=discord.ButtonStyle.primary)
    async def nasdaq_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        etf = yf.Ticker('^NDX')  # Nasdaq 100
        price = etf.history(period='1d')['Close'].iloc[-1]
        history = etf.history(period='1y')

        await interaction.response.send_message(f"{interaction.user.mention}, the current price of Nasdaq 100 is €{price:.2f}")

        # Create a graph of the Nasdaq 100 price history
        fig, ax = plt.subplots()
        ax.plot(history.index, history['Close'], label='Close Price', color='orange')
        ax.set(xlabel='Date', ylabel='Price (EUR)', title='Nasdaq 100 Price History (EUR)')
        ax.grid()
        ax.legend()

        # Save the graph to a bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Send the graph as an attachment
        await interaction.channel.send(file=discord.File(fp=buf, filename='nasdaq_price_history.png'))
        plt.close(fig)

    @discord.ui.button(label="MSCI World", style=discord.ButtonStyle.primary)
    async def msci_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        etf = yf.Ticker('ACWI')  # MSCI World
        price = etf.history(period='1d')['Close'].iloc[-1]
        history = etf.history(period='1y')

        await interaction.response.send_message(f"{interaction.user.mention}, the current price of MSCI World is €{price:.2f}")

        # Create a graph of the MSCI World price history
        fig, ax = plt.subplots()
        ax.plot(history.index, history['Close'], label='Close Price', color='green')
        ax.set(xlabel='Date', ylabel='Price (EUR)', title='MSCI World Price History (EUR)')
        ax.grid()
        ax.legend()

        # Save the graph to a bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Send the graph as an attachment
        await interaction.channel.send(file=discord.File(fp=buf, filename='msci_price_history.png'))
        plt.close(fig)

class ETFsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('ETFsCog is ready')

    @commands.command()
    async def etfs(self, ctx):
        view = ETFsView()
        await ctx.send(f"{ctx.author.mention}, select an ETF:", view=view)

async def setup(bot):
    await bot.add_cog(ETFsCog(bot))
