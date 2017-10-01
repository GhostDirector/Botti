from random import randint

class TicTacToe:

    __board = []

    def __init__(self):
        print("TicTacToe initialized")
        for i in range(9):
            self.__board.append("#")

    def sendBoard(self):
        return self.__board

    def testPrint(self):
        for x in range(0, len(self.__board)):
            print(self.__board[x])
        print("########################################################")

    def resetGame(self):
        for x in range(0, len(self.__board)):
            self.__board[x] = "#"


    def makeMove(self, spot):
        emptycount = 0
        if self.isValid(spot) and self.isFree(spot):
            self.__board[spot] = "o"
            for i in range(0, len(self.__board)):
                if i == "-":
                    emptycount = emptycount + 1
            while True:
                if emptycount is 1:
                    return True
                tmp = self.botMove()
                if self.isFree(tmp):
                    self.__board[tmp] = "x"
                    return True
        return False

    def checkWinner(self):
        print()

    def isFree(self, spot):
        if self.__board[spot] == "#":
            return True

    def isValid(self, spot):
        if spot >= 0 and spot <= 8:
            return True

    def botMove(self):
        return randint(0, 8)

    def Main(self):
        self.resetGame()
        self.sendBoard()
