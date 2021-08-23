import os
import discord
from random import randint

from discord import message
# from dotenv import load_dotenv

# load_dotenv()
TOKEN = ''

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello')


client.run(TOKEN)


def roll(amount):
    results = []
    for i in range(0,amount):
        results.append(randint(1,6))
        while results[-1] % 6 == 0:
            results[-1] = results[-1] + randint(1,6)
    return results