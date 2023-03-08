"""One Shot Wordle."""

__author__ = "730572303"

SECRET: str = "python"
guess: str = (input("What is your 6-letter guess? "))
playing: bool = True
count: int = 0
number_tries: int = 0
guessidx: int = 0
idx: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(SECRET):
    guess = input("That was not 6 letters! Try again: ")
while guessidx < len(SECRET):
    if SECRET[guessidx] == guess[guessidx]:
        idx = idx + GREEN_BOX
    else:
        bool = False
        index = 0
        while bool is False and index < len(SECRET):
            if SECRET[index] == guess[guessidx]:
                bool = True
            else:
                index = index + 1
        if bool is True:
            idx = idx + YELLOW_BOX
        else:
            idx = idx + WHITE_BOX
    guessidx = guessidx + 1
print(idx)
if guess == SECRET:
    print("Woo! You got it!")
if guess != SECRET:
    print("Not quite. Play again soon!")