import discord
from discord.ext import tasks
import random


TOKEN = "ここにボットのトークン"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

CHANNEL_ID = 000#ここにチャンネルid
USER_ID = 000#ここにユーザーid
@client.event
async def on_ready():
  print(f'{client.user}がログインしました') 
  await tree.sync()
  mugen.start()

@tasks.loop(seconds = 1200)
async def mugen():
  magure = random.randint(0,2)
  print(magure)
  if magure == 1:
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(f"<@{USER_ID}>水を飲む時間です")

client.run(TOKEN)
