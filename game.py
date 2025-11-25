from random import randint
import time


class Game:
    DIFFICULTY_SETTINGS = {
        "1": {"difficulty": "easy", "maxGuessChances": 10},
        "2": {"difficulty": "medium", "maxGuessChances": 5},
        "3": {"difficulty": "hard", "maxGuessChances": 3},
    }

    def __init__(self):
        self._difficultyLevel: str = ""
        self._userGuessCount: int = 0
        self._maxGuessCount: int = 0
        self._cpuGuess: int = 0
        self._isGameOver: bool = False

    def setDifficultyLevel(self, choice) -> None:
        while choice not in Game.DIFFICULTY_SETTINGS:
            print("Invalid choice selected. Let's try again.\n")
            choice = input("Please select a difficulty level: ")

        self._difficultyLevel = Game.DIFFICULTY_SETTINGS[choice]["difficulty"]
        self._maxGuessCount = Game.DIFFICULTY_SETTINGS[choice]["maxGuessChances"]

    def _getValidInput(self) -> int:
        is_valid = False

        number = None
        while not is_valid:
            user_input = input("Enter your guess: ")
            if user_input.isdigit():
                number = int(user_input)
                is_valid = True
            else:
                print("Invalid input!\n")

        return number

    def _setup(self) -> None:
        self._cpuGuess = randint(1, 100)
        self._userGuessCount = 0
        self._isGameOver = False

    def _resetGame(self) -> None:
        if self._getUserResponse("\nPlay again (yes/no): "):
            self.play()
        else:
            print("👋 Goodbye! Thanks for playing!\n")

    def _hint(self) -> None:
        lowBound = max(1, self._cpuGuess - 10)
        highBound = min(100, self._cpuGuess + 10)

        print(f"💡 Hint 1: The number is between {lowBound} and {highBound}")

        output = "even" if self._cpuGuess % 2 == 0 else "odd"
        print(f"💡 Hint 2: The number is {output}\n")

    def _should_offer_hint(self):
        remainingGuessLeft = self._maxGuessCount - self._userGuessCount
        return remainingGuessLeft <= 2 and not self._isGameOver

    def _getUserResponse(self, prompt: str) -> bool:
        while True:
            user_response = input(prompt).strip().lower()

            if user_response in ("y", "yes"):
                return True
            elif user_response in ("n", "no"):
                return False
            else:
                print("Please enter '(y)es' or '(n)o'")

    def play(self) -> None:
        self._setup()
        self._printMenu()
        start = time.time()

        while not self._isGameOver and self._userGuessCount < self._maxGuessCount:
            user_guess = self._getValidInput()
            self._userGuessCount += 1

            if self._cpuGuess < user_guess:
                print(f"❌ Incorrect! The number is less than {user_guess}.\n")
            elif self._cpuGuess > user_guess:
                print(f"❌ Incorrect! The number is greater than {user_guess}.\n")
            else:
                print(
                    f"🎉 Congratulations! You guessed the correct number in {self._userGuessCount} attempt(s). 🔥🔥"
                )
                self._isGameOver = True

            if self._userGuessCount < self._maxGuessCount and self._should_offer_hint():
                if self._getUserResponse("🤔 Stuck? Need a helping hand (yes/no): "):
                    self._hint()

        if not self._isGameOver and self._userGuessCount == self._maxGuessCount:
            print(f"💀 Game over! The number was {self._cpuGuess}.")
            self._isGameOver = True

        if self._isGameOver:
            print(f"Game Time: {self._timeElapsed(start, time.time())} seconds")
            self._resetGame()

    def _timeElapsed(self, start, end) -> int:
        return int(end - start)

    def _printMenu(self) -> None:
        print()
        print("*" * 50)
        print("Welcome to the Number Guessing Game!")
        print("*" * 50)
        print("I'm thinking of a number between 1 and 100.")

        print("Please select the difficulty level:")
        print(f"1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")

        print("Enter your choice: ", end="")
        self.setDifficultyLevel(input().strip())

        print()
        print(
            f"Great! You have selected the {self._difficultyLevel.capitalize()} difficulty level."
        )
        print("Let's start the game!\n")

    def __str__(self):
        return f"Secret Number: {self._cpuGuess}\nDifficulty: {self._difficultyLevel}"
