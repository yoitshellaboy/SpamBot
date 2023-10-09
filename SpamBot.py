import discord
from discord import Client, Activity, ActivityType
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

client = discord.Client(intents=intents)
bot = commands.Bot(
    command_prefix = '!',
    intents=intents,
    activity = Activity(type=ActivityType.playing, name='funny henti games')
)

@bot.command(name='spam', help='Spams the input message for x number of times')
async def spam(ctx, amount:int, *, message):
    for i in range(amount): # Do the next thing amount times
        await ctx.send(message) # Sends message where command was called

bot.run('TOKEN HERE')