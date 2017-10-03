from random import randint


class Dice:
    def __init__(self):
        self.min = 1
        self.max = 100

    def print_roll(self, min, max):
        result = randint(min, max)
        text = "(" + str(min) + "-" + str(max) + ") Result: " + str(result)
        return text

    def roll(self):
        return self.print_roll(self.min, self.max)

    def set_min(self, min):
        if min > 1:
            self.min = min
        else:
            self.min = 1

    def set_max(self, max):
        if max > 1:
            self.max = max
        else:
            self.max = 1
