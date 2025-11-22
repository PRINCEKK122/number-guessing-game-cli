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

    def setDifficultyLevel(self, choice):
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
                print("Invalid choice selected. Let's try again\n")
                choice = input("Please select a difficulty level: ")

    def play(self, guess: str):
        if not guess.isdigit():
            raise ValueError("Please enter a valid digit")

        while self._userGuessCount < self._maxGuessCount:
            if guess < self._cpuGuess:
                print(f"Incorrect! The number is less than {self._cpuGuess}.")
                self._userGuessCount += 1
            elif guess > self._cpuGuess:
                print(f"Incorrect! The number is greater than {self._cpuGuess}.")
                self._userGuessCount += 1
            else:
                print(
                    f"Congratulation! You guessed the correct number in {self._userGuessCount} attempts."
                )

    def print_menu(self):
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print("You have 5 chances to guess the correct number")
        print()
        print("Please select the difficulty level:")
        print(f"1. Easy (10 chances)\n2. Medium (5 chances)\nHard (3 chances)")
        print()
        print("Enter your choice: ", end="")
        self.setDifficultyLevel(input().strip())

    def __str__(self):
        return f"CPU Guess: {self._cpuGuess}\nGame Difficulty: {self._difficultyLevel}"
