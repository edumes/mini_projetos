import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')


@client.event
async def on_ready():
  print('Join {0.user}'.format(client))

@client.command()
async def ola(ctx):
  await ctx.send('boa noite bruno')










client.run('ODgwMjIwMTcwODMwODc2Nzcy.YSbG6g.IB1dtNAszKeFAdmTwwtS6T9pHr4')