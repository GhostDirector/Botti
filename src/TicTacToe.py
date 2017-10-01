from random import randint

class TicTacToe:

    __board = []

    def __init__(self):
        for i in range(9):
            self.__board.append('-')

    def sendBoard(self):
        print()

    def testPrint(self):
        for x in range(0, len(self.__board)):
            print(self.__board[x])
        print("########################################################")

    def resetGame(self):
        for x in range(0, len(self.__board)):
            self.__board[x] = '-'


    def makeMove(self, spot):
        if self.isValid(spot) & self.isFree(spot):
            self.__board[spot] = 'O'
            while True:
                tmp = self.botMove()
                if self.isFree(tmp):
                    self.__board[tmp] = 'X'
                    break

    def checkWinner(self):
        print()

    def isFree(self, spot):
        if self.__board[spot] == '-':
            return True

    def isValid(self, spot):
        if spot >= 0 & spot <= 8:
            return True

    def botMove(self):
        return randint(0, 8)

    def Main(self):
        self.resetGame()
        self.sendBoard()

if __name__ == "__main__":
    game = TicTacToe()
    game.resetGame()
    game.testPrint()
    game.makeMove(4)
    game.testPrint()
    game.makeMove(5)
    game.testPrint()
