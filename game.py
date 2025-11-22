from random import randint

class Game:
    def __init__(self):
        self._isRunning = True
        self._cpuGuess = randint(1, 100)
        self._difficultyLevel = ("easy", "medium", "level")
        self._userGuessCount = 0

    def getCpuGuess(self):
        return self._cpuGuess
