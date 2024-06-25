"""Set 3, Exercise 2.

An example of how a guessing game might be written.
Play it through a few times, but also stress test it. What if your lower bound 
is 🍟, or your guess is "pencil", or "seven"
This will give you some intuition about how to make exercise 3 more robust.
"""

import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nWelcome to the guessing game!")  # The string is printed in a new line
    print("A number between 0 and _ ?")
    upperBound = input("Enter an upper bound: ")  # prompt the user to input a number
    print(
        f"OK then, a number between 0 and {upperBound} ?"
    )  # confirms upper bound entered by user
    upperBound = int(upperBound)  # turns the input into an integer

    actualNumber = random.randint(
        0, upperBound
    )  # generates random number between 0 and upper bound

    guessed = False  # a variable is made which is used later in the loop

    while not guessed:  # starts a loop which starts everytime guessed = False
        guessedNumber = int(
            input("Guess a number: ")
        )  # prompts user to guess a number then turns it into an input
        print(f"You guessed {guessedNumber},")  # confirms guessed Number
        if (
            guessedNumber == actualNumber
        ):  # checks if guessed number equals actual number
            print(
                f"You got it!! It was {actualNumber}"
            )  # confirms it is the right number
            guessed = True  # sets guessed as True, which stops the loop
        elif (
            guessedNumber < actualNumber
        ):  # if the guessed number is less than the actual number, it will tell it is too small
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"


if __name__ == "__main__":
    exampleGuessingGame()
