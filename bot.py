import discord
from discord.ext import commands

# Create an instance of a bot with a command prefix
intents = discord.Intents.default()
intents.message_content = True  # This allows the bot to read message content
bot = commands.Bot(command_prefix='!', intents=intents)

# Event that triggers when the bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="A discord server"))

# Run the bot with your token
bot.run('Bot Token Here')
