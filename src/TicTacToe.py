from random import randint

class TicTacToe:

    __board = []

    def __init__(self):
        print("TicTacToe initialized")
        for i in range(9):
            self.__board.append("#")

    def sendBoard(self):
        return self.__board

    def resetGame(self):
        for x in range(0, len(self.__board)):
            self.__board[x] = "#"


    def makeMove(self, spot):
        if self.isValid(spot) and self.isFree(spot):
            self.__board[spot] = "o"
            return True
        return False


    def isFree(self, spot):
        if self.__board[spot] == "#":
            return True

    def isValid(self, spot):
        if spot >= 0 and spot <= 8:
            return True

    def botMove(self):
        while True:
            print("test")
            tmp = randint(0, 8)
            if self.isFree(tmp):
                self.__board[tmp] = "x"
                break


    def checkLast(self):
        if "#" not in self.__board:
            return True
        else:
            return False

    def status(self):
        tmp = ""
        for i in range(0, len(self.__board)):
            if i == 2:
                tmp = tmp + self.__board[i] + "\n"
            elif i == 5:
                tmp = tmp + self.__board[i] + "\n"
            elif i == 8:
                tmp = tmp + self.__board[i]
            else:
                tmp = tmp + self.__board[i] + ""
        return tmp

    def get__board(self):
        return self.__board

    def cheat(self):
        for x in range(0, len(self.__board)):
            self.__board[x] = "o"