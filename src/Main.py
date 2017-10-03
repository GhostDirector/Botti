import discord
import asyncio
import src.Dice
from discord.ext.commands import Bot
from discord.ext import commands

class Disco:
    # Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
    global client, dice
    client = Bot(description="DISCOBOT 2000", command_prefix="-", pm_help=True)
    dice = src.Dice.Dice()

    # Suorittaa tämän metodin aina käynnistyksessä
    @client.event
    async def on_ready(*args):
        print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
            len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
        print('HELLO')


    # Tekstin tulostus
    @client.command()
    async def testPrint(*args):
        await client.say("Testing")
        await asyncio.sleep(3)
        await client.say("Another testing")

    @client.command()
    async def testPrint2(*args):
        await client.say("Testing2")

    @client.command()
    async def roll( *args):
        dice.roll()

    client.run('MzYyMTc2Mjc5MjM3MjMwNTky.DKu2hQ.opMSFRUxngL_P1uNMjN5gyVHdd8')

if __name__ == "__main__":
    Disco()
