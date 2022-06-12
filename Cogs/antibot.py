import discord
import os
from discord.ext import commands

class antibot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(member):
      guild = member.guild
      owner = guild.owner
      reason = "Darkz Sec | Anti-Bot-Add"
      logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add).flatten()
      logs = logs[0]
      if logs.user == owner:
      	pass
      else:
       if member.bot:
        await member.ban(reason=f"{reason}")
        await logs.user.ban(reason=f"{reason}")
