import discord
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
print(DISCORD_TOKEN)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    print(message.author)
    if "badr" in message.author.name:
        await message.channel.send("badr has spoken")
    if "Akurafu" in  message.author.name  :
        await message.channel.send("Achraf u know that ur friends hate u :'(")
    if "Kawa" in  message.author.name  :
        await message.channel.send("o kawaii koto ~~")
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        await message.channel.send(message.content)
        print(message.content)

client.run(DISCORD_TOKEN)