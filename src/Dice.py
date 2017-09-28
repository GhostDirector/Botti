from random import randint


class Dice:
    def __init__(self):
        self.min = 1
        self.max = 100

    def print_roll(self, min, max):
        print("(", min, "-", max, ") Result: ", randint(min, max))

    def roll(self):
        self.print_roll(self.min, self.max)

    