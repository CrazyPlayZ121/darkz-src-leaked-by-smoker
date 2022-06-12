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
import random

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class antirole(commands.Cog):
    def __init__(self, client):
        self.client = client      
        self.headers = {"Authorization": "Bot ODUyOTE5NDIzMDE4NTk4NDMw.YMN1HA.8tV15ZUok2ps-162jeRCE0khiQ4"}
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        try:
          guild = role.guild
          reason = "Darkz Security | Anti Role Create"
          logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create).flatten()
          logs = logs[0]
          user = logs.user.id
          api = random.randint(8,9)
          if logs.user.id == 852919423018598430:
            return
          elif user == guild.owner:
            pass
          else:
            async with aiohttp.ClientSession(headers=self.headers) as session:
              async with session.put(f"https://discord.com/api/v{api}/guilds/%s/bans/%s" % (guild.id, user), json={"reason": reason}) as r:
                await role.delete()
                took = round((datetime.now().timestamp() - start), 3)
                log = await r.text()
                if r.status in (200, 201, 204):
                            	logging.info("Successfully banned %s" % (user))
        except Exception as error:
            logging.error(error)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        try:
          guild = role.guild
          reason = "Darkz Security | Anti Role Delete"
          logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete).flatten()
          logs = logs[0]
          user = logs.user.id
          api = random.randint(8,9)
          if logs.user.id == 852919423018598430:
            return
          elif user == guild.owner:
            pass
          else:
            async with aiohttp.ClientSession(headers=self.headers) as session:
              async with session.put(f"https://discord.com/api/v{api}/guilds/%s/bans/%s" % (guild.id, user), json={"reason": reason}) as r:
                took = round((datetime.now().timestamp() - start), 3)
                log = await r.text()
                await guild.create_role(reason="Darkz Security | Role Recovery", name=f"{role}")
                if r.status in (200, 201, 204):
                            	logging.info("Successfully banned %s" % (user))
        except Exception as error:
            logging.error(error)
    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
      try:
        guild = after.guild
        reason = "Darkz Security | Anti Role Update"
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_update).flatten()
        logs = logs[0]
        user = logs.user.id
        api = random.randint(8,9)
        if logs.user.id == 925705956757741609:
            return
        elif user == guild.owner:
          pass
        else:
          
          async with aiohttp.ClientSession(headers=self.headers) as session:
              async with session.put(f"https://discord.com/api/v{api}/guilds/%s/bans/%s" % (guild.id, user), json={"reason": reason}) as r:
                await after.edit(name=f"{before.name}")
                took = round((datetime.now().timestamp() - start), 3)
                log = await r.text()
                if r.status in (200, 201, 204):
                            	logging.info("Successfully banned %s" % (user))
      except Exception as error:
            logging.error(error)

