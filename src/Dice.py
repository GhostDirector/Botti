from random import randint


class Dice:
    def __init__(self):
        min = 1
        max = 100

    def print(self, min, max):
        print("(", min, "-", max, ") Result: ", randint(min, max))

    