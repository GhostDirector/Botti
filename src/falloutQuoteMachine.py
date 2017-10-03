from random import randint
import linecache

class falloutQuoteMachine:

    def __init__(self):
        print("FalloutQuoteMachine initialized")

    def quote(self):
        tmp = randint(0, 21)
        return linecache.getline('FalloutQuotes.txt', tmp)
