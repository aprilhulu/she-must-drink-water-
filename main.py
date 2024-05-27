import discord
from discord.ext import tasks
from discord import app_commands
import random
import os
from pathlib import Path
import json

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
paths = "channel.json"
p0 = Path(paths)
is_file = os.path.isfile(paths)


if is_file:
  json_open = open('channel.json', 'r')
  json_data = json.load(json_open)
  json_op = open('token.json','r')
  json_da = json.load(json_op)
  json_pn =open('user.json','r')
  json_dt = json.load(json_pn)
  TOKEN = json_da['TOKEN']
  CHANNEL_ID = json_data['CHANNEL']
  USER_ID = json_dt['USER']
  
  @client.event
  async def on_ready():
    print(f'{client.user}がログインしました') 
    await tree.sync()
    mugen.start()

  @tree.command(name="stop", description="通知の停止コマンドです ")
  async def stop(interaction: discord.Interaction):
      mugen.cancel()
      await interaction.response.send_message("停止しました")


  @tasks.loop(seconds = 1200)
  async def mugen():
     magure = random.randint(0,2)
     print(magure)
     if mugen == 1:
         channel = client.get_channel(CHANNEL_ID)
         await channel.send(f"<@{USER_ID}>水を飲む時間です")
  client.run(TOKEN)

else:
  p0.touch()
  token = input("discordbotトークンを入力してください")
  use =  input("ユーザーIDを入力してください")
  chs = input("チャンネルIDを入力してください")
  memo =  {
          "CHANNEL":int(chs)
          }
  mono = {
          "TOKEN":token
          }
  mome = {
          "USER":int(use)
          }
  with open("channel.json", "w") as f:
        json.dump(memo, f)
  with open("token.json", "w") as f:
        json.dump(mono, f)
  with open("user.json", "w") as f:
        json.dump(mome, f)
