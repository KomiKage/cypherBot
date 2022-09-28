import json
import disnake
from disnake.ext import commands

with open('config.json', 'r') as configJson:
    config = json.load(configJson)

bot = commands.Bot()

client = disnake.Client()

@client.event
async def on_ready():
    print(f'{client.user} : Time to work.. (╥﹏╥)')

client.run(config["token"])