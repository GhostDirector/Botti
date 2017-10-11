from random import randint


class Dice:
    def __init__(self):
        self.min = 1
        self.max = 100

    def roll(self, args):
        if len(args) >= 2:
            self.set_min(args[0])
            self.set_max(args[1])
        elif len(args) == 1:
            self.set_max(args[0])

        if self.min <= self.max:
            result = randint(self.min, self.max)
        else:
            result = randint(self.max, self.min)

        text = "(" + str(self.min) + "-" + str(self.max) + ") Result: " + str(result)
        return text

    def set_min(self, min):
        try:
            min = int(min)
        except ValueError:
            min = 1

        if min > 1:
            self.min = min
        else:
            self.min = 1

    def set_max(self, max):
        try:
            max = int(max)
        except ValueError:
            max = 1

        if max > 1:
            self.max = max
        else:
            self.max = 1
