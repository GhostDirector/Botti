import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="DISCOBOT 2000", command_prefix="-", pm_help=True)


# Suorittaa tämän metodin aina käynnistyksessä
@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
        len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('HELLO')


# Tekstin tulostus
@client.command()
async def tulosta(*args):
    await client.say("TEXT")
    await asyncio.sleep(3)
    await client.say("ANOTHER TEXT")

client.run('MzYyMTc2Mjc5MjM3MjMwNTky.DKu2hQ.opMSFRUxngL_P1uNMjN5gyVHdd8')

