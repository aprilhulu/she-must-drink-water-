import discord
from discord.ext import tasks
import random


TOKEN ="トークンを貼る"

CHANNEL_ID = #チャンネルIDをはる

USER_ID = #ユーザーIDを貼る

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'{client.user}がログインしました') 
  mugen.start()

@tasks.loop(seconds = 1200)
async def mugen():
  magure = random.randint(0,2)
  print(magure)
  if magure == 1:
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(f"<@{USER_ID}>水を飲む時間です")

client.run(TOKEN)
