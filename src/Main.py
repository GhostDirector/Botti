import discord
import asyncio
import src.Dice
import src.TicTacToe

from discord.ext.commands import Bot
from discord.ext import commands

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

    @client.command()
    async def commands(*args):
        await client.say("-testPrint\n"
                         "-ttt #play tic tac toe\n"
                         "-roll #roll 1-100 or -roll number for 1-number or -roll number number for number-number")


    # Tekstin tulostus
    @client.command()
    async def testPrint(*args):
        await client.say("Testing")
        await asyncio.sleep(3)
        await client.say("Another testing")

    @client.command()
    async def ttt(*args):
        if len(args) >= 1:
            if args[0].isdigit():
                if int(args[0]) >= 0:
                    if int(args[0]) <= 9:
                        if ticTacToe.makeMove(int(args[0]) - 1):
                            await client.say("Move made")
                            if ticTacToe.checkLast() == True:
                                await client.say(ticTacToe.status())
                                await client.say("Game over")
                            else:
                                ticTacToe.botMove()
                                await client.say(ticTacToe.status())


            elif args[0] == "status":
                await client.say(ticTacToe.status())
            elif args[0] == "reset":
                ticTacToe.resetGame()
            elif args[0] == "help":
                await client.say("Arguments: 1-9 (make move) | status (display game status) | reset (resets game)")
            elif args[0] == "test":
                await client.say(ticTacToe.get__board())
            elif args[0] == "cheat":
                ticTacToe.cheat()
                await client.say(ticTacToe.status())
                await client.say("Ultimate win!")


    @client.command()
    async def roll(*args):
        dice = src.Dice.Dice()
        text = str(dice.roll(args))
        await client.say(text)

    @client.command()
    async def cat(*args):
        await client.say("https://www.catgifpage.com/")

    client.run('MzYyMTc2Mjc5MjM3MjMwNTky.DKu2hQ.opMSFRUxngL_P1uNMjN5gyVHdd8')

if __name__ == "__main__":
    Disco()
