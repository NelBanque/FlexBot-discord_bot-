import discord
from discord.ext import commands
import yfinance as yf
import matplotlib.pyplot as plt
import io

class ActionsView(discord.ui.View):
    @discord.ui.button(label="Apple", style=discord.ButtonStyle.primary)
    async def apple_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        stock = yf.Ticker('AAPL')  # Apple
        price = stock.history(period='1d')['Close'].iloc[-1]
        history = stock.history(period='1y')

        await interaction.response.send_message(f"{interaction.user.mention}, the current price of Apple is €{price:.2f}")

        # Create a graph of the Apple price history
        fig, ax = plt.subplots()
        ax.plot(history.index, history['Close'], label='Close Price', color='blue')
        ax.set(xlabel='Date', ylabel='Price (EUR)', title='Apple Price History (EUR)')
        ax.grid()
        ax.legend()

        # Save the graph to a bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Send the graph as an attachment
        await interaction.channel.send(file=discord.File(fp=buf, filename='apple_price_history.png'))
        plt.close(fig)

    @discord.ui.button(label="Microsoft", style=discord.ButtonStyle.primary)
    async def microsoft_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        stock = yf.Ticker('MSFT')  # Microsoft
        price = stock.history(period='1d')['Close'].iloc[-1]
        history = stock.history(period='1y')

        await interaction.response.send_message(f"{interaction.user.mention}, the current price of Microsoft is €{price:.2f}")

        # Create a graph of the Microsoft price history
        fig, ax = plt.subplots()
        ax.plot(history.index, history['Close'], label='Close Price', color='green')
        ax.set(xlabel='Date', ylabel='Price (EUR)', title='Microsoft Price History (EUR)')
        ax.grid()
        ax.legend()

        # Save the graph to a bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Send the graph as an attachment
        await interaction.channel.send(file=discord.File(fp=buf, filename='microsoft_price_history.png'))
        plt.close(fig)

    @discord.ui.button(label="Amazon", style=discord.ButtonStyle.primary)
    async def amazon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        stock = yf.Ticker('AMZN')  # Amazon
        price = stock.history(period='1d')['Close'].iloc[-1]
        history = stock.history(period='1y')

        await interaction.response.send_message(f"{interaction.user.mention}, the current price of Amazon is €{price:.2f}")

        # Create a graph of the Amazon price history
        fig, ax = plt.subplots()
        ax.plot(history.index, history['Close'], label='Close Price', color='orange')
        ax.set(xlabel='Date', ylabel='Price (EUR)', title='Amazon Price History (EUR)')
        ax.grid()
        ax.legend()

        # Save the graph to a bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Send the graph as an attachment
        await interaction.channel.send(file=discord.File(fp=buf, filename='amazon_price_history.png'))
        plt.close(fig)

class ActionsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('ActionsCog is ready')

    @commands.command()
    async def actions(self, ctx):
        view = ActionsView()
        await ctx.send(f"{ctx.author.mention}, select a stock:", view=view)

async def setup(bot):
    await bot.add_cog(ActionsCog(bot))
