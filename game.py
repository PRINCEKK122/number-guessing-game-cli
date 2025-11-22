from random import randint


class Game:
    def __init__(self):
        self._isRunning = True
        self._cpuGuess = randint(1, 100)
        self._difficultyLevel = ""
        self._userGuessCount = 0
        self._maxGuessCount = 0

    def get_cpu_guess(self):
        return self._cpuGuess

    def getDifficultyLevel(self):
        return self._difficultyLevel

    def setDifficultyLevel(self):
        prompt = "Please select a difficulty level: "
        choice = input(prompt).strip()

        is_valid = False
        while not is_valid:
            if choice == "1":
                self._difficultyLevel = "easy"
                self._maxGuessCount = 10
                is_valid = True
            elif choice == "2":
                self._difficultyLevel = "medium"
                self._maxGuessCount = 5
                is_valid = True
            elif choice == "3":
                self._difficultyLevel = "hard"
                self._maxGuessCount = 3
                is_valid = True
            else:
                print("Invalid choice selected. Let's try again")
                choice = input(prompt)

    def play(self, guess):
        pass

    def __str__(self):
        return f"CPU Guess: {self._cpuGuess}\nGame Difficulty: {self._difficultyLevel}"
