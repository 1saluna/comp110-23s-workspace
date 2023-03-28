"""Guess the number."""

__author__ = "730572303"

from random import randint

SECRET: int = randint(1, 100)
YAY: str = "\U0001F973"
PLAY: str = "\U0001F913"
CLOSE: str = "\U0001F9D0"

guess: int 
points: int = 0
playing: bool = True
result: bool = False
turns: int = 2
player: str = ""


def greet() -> None:
    """Greets the player and gets their name."""
    player: str = input("Hello! What is your name? ")
    print(f"Welcome {player}! Let's play Guess the Number!")
    print("Here are the rules:")
    print("1. Keep guessing the number until you get it right!")
    print("2. The number must be between 1 and 100.")
    print("3. The game will keep playing until you guess the correct number unless you type 'STOP'.")
    print("4. The more guesses you take, the more points you will get (try to get as little points as possible!).")
    print("5. HAVE FUN AND GOOD LUCK!")


def oddeven() -> None:
    """Tells the player if the guess is odd or even."""
    global guess
    global playing
    global turns
    if guess == SECRET:
        correct()
    else:
        while SECRET % 2 == 0 and guess != SECRET and guess != 0:
            if guess % 2 == 0:
                clue = "You're on the right track... the guess is even!"
                print(clue)
                correct()
            else:
                clue = "Your guess was odd... the secret number is even!"
                print(clue)
                correct()
        while SECRET % 2 != 0 and guess != SECRET and guess != 0:
            if guess % 2 != 0:
                clue = "You're on the right track... the guess is odd!"
                print(clue)
                correct()
            else:
                clue = "Your guess was even... the secret number is odd!"
                print(clue)
                correct()


def question() -> int:
    """Starts the game and checks to see if the person wants to play."""
    print("----You are on your first turn.----")
    guess: int = int(input("Guess a number (1 - 100): "))
    if guess == 0:
        print("You ended the game :( Goodbye!")
        end()
    if playing is True:
        return guess
    return guess


def correct() -> bool: 
    """Checks to see if the players guess is correct."""
    global result
    global guess
    global turns
    global points
    if guess != SECRET:
        num_points(points)
        points = num_points(points)
        print(f"You have {points} points. Keep going!")
        print(f"----You are on turn number {turns}.----")
        guess = int(input(f"{PLAY}Try again: "))
        if guess == 0:
            print("You ended the game :( Goodbye!")
            end()
        turns += 1
        return result
    if guess == SECRET:
        num_points(points)
        print(f"You have completed the game with {points} points! {YAY} Try to get a lower number next time...")
        result = True
    return result


def stop() -> None:
    """If the player types anything other than 'yes' the game wont play."""
    print("Type 'yes' to play, if not type anything else...")
    decision: str = input("Would you like to play the game? ")
    if decision != "yes":
        print("You ended the game :( Goodbye!")
        end()


def num_points(points: int) -> int:
    """Calculates the amount of points for each turn."""
    points += 1
    return points


def end() -> None:
    """Stops the game."""
    global playing
    print("Thank you for playing!")
    playing = False


def main() -> None:
    """Plays the game while calling the other functions."""
    global playing
    global guess
    global points
    stop()
    while playing is True:
        greet()
        guess = question()
        oddeven()
        if guess == SECRET:
            correct()
            end()


if __name__ == "__main__":
    """Calls main."""
    main()