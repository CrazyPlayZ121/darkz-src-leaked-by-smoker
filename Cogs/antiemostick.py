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

class antiemostick(commands.Cog):
    def __init__(self, client):
        self.client = client      
        self.headers = {"Authorization": "Bot ODUyOTE5NDIzMDE4NTk4NDMw.YMN1HA.8tV15ZUok2ps-162jeRCE0khiQ4"}
    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        try:
            guild = after.guild
            reason = "Darkz Security | Anti Emoji Create"
            logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.emoji_create).flatten()
            logs = logs[0]
            user = logs.user.id
            api = random.randint(8,9)
            async with aiohttp.ClientSession(headers=self.headers) as session:
              async with session.put(f"https://discord.com/api/v{api}/guilds/%s/bans/%s" % (after.id, user), json={"reason": reason}) as r:
                took = round((datetime.now().timestamp() - start), 3)
                log = await r.text()
                if r.status in (200, 201, 204):
                            	logging.info("Successfully banned %s" % (user))
        except Exception as error:
            logging.error(error)
          #dm dekh