from random import randint

class TicTacToe:

    __board = [3][3]

    def sendBoard(self):
        print()

    def resetGame(self):
        for i in self.__board:
            for j in self.__board:
                self.__board[i][j] = '-'


    def makeMove(self, row, col):
        if self.isValid(row, col) & self.isFree(row, col):
            self.__board[row][col] = 'O'

    def checkWinner(self):
        print()

    def isFree(self, row, col):
        if self.__board == '-':
            return True

    def isValid(self, row, col):
        if row >= 0 & row <= 3:
            if row >= 0 & row <= 3:
                return True

    def botMove(self):
        self.__board[randint(0, 2)][randint(0, 2)]
