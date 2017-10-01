import discord
import asyncio
import src.TicTacToe
from discord.ext.commands import Bot
from discord.ext import commands


def status():
    tmp = ""
    board = ticTacToe.sendBoard()
    for i in range(0, len(board)):
        if i == 2:
            tmp = tmp + board[i] + "\n"
        elif i == 5:
            tmp = tmp + board[i] + "\n"
        elif i == 8:
            tmp = tmp + board[i]
        else:
            tmp = tmp + board[i] + ""
    return tmp


class Disco:
    # Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
    global client, ticTacToe
    client = Bot(description="DISCOBOT 2000", command_prefix="-", pm_help=True)
    ticTacToe = src.TicTacToe.TicTacToe()


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
    async def ttt(*args):
        if args[0].isdigit():
            if int(args[0]) >= 0:
                if int(args[0]) <= 9:
                    ticTacToe.makeMove(int(args[0]) - 1)
                await client.say("Move made")
                await client.say(status())

        elif args[0] == "status":

            await client.say(status())

    client.run('MzYyMTc2Mjc5MjM3MjMwNTky.DKu2hQ.opMSFRUxngL_P1uNMjN5gyVHdd8')

if __name__ == "__main__":
    Disco()
