"""EX03 Wordle."""

__author__ = "730572303"

SECRET: str = "codes"

def contains_char(word: str, character: str) -> bool: #  uses contains_char to see if the character is in the word
    index: int = 0
    contains: bool = False
    assert len(character) == 1
    while index < len(word):
        if word[index] == character:
            contains = True
        index = index + 1
    return contains

def emojified(guess: str, SECRET: str) -> str: #  shows if the character is in the word or in the right space using emojis
    """Using emojis to see if the character is in the word."""
    guess_index: int = 0
    idx: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(SECRET)
    while guess_index < len(SECRET):
        if guess[guess_index] == SECRET[guess_index]:
            idx = idx + GREEN_BOX
        else: 
            if contains_char(SECRET, guess[guess_index]) is True:
                idx = idx + YELLOW_BOX
            if contains_char(SECRET, guess[guess_index]) is False:
                idx = idx + WHITE_BOX
        guess_index = guess_index + 1
    return idx

def input_guess(expected_length: int) -> str: #  Sees if the word is the same length as the secret word
    """Seeing if the word is the correct length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That was not {expected_length} chars! Try again: ")
    return guess

def main() -> None: #  calls the function and plays the game
    """The entrypoint of the program and main game loop."""
    N: int = 1
    expected_length: int = len(SECRET)
    playing: bool = True
    while N <= 6 and playing == True:
        print("=== Turn " + str(N) + "/6 ===")
        guess: str = input_guess(len(SECRET))
        if guess == SECRET:
            print(emojified(guess, SECRET))
            print("You won in " + str(N) + "/6 turns!")
            playing = False
        else:
            print(emojified(guess, SECRET))
        N = N + 1
    if N > 6:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__": #  calls main()
    main()