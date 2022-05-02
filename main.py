import discord
from discord.ext import commands

token = "" #ใส่ token ตรงนี้

bot = commands.Bot(command_prefix = "NICEDAYFORFREEEIEI")

status = input(' > ')

@bot.event
async def on_connect():
    stream = discord.Streaming(
        name = status,
        url = 'https://www.twitch.tv/monstercat' #ใส่ url twitch
    )
    print('Streaming: ' + status)
    await bot.change_presence(activity=stream)

bot.run(token, bot=False)  