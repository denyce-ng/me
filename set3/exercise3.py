"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")  # The string is printed in a new line
    print("Give me a number.")
    lowerBound = input("Enter an integer: ")  # prompt the user to input a number
    while True:
        try:
            lowerBound = int(lowerBound)
            break
        except ValueError as input_error:
            lowerBound = input(f"This is not a valid integer. Give me a valid integer:")
    print(f"Give me another number larger than {lowerBound}.")

    upperBound = input(f"Enter an integer larger than {lowerBound}:")
    while True:
        try:
            upperBound = int(upperBound)
            if upperBound > lowerBound:
                break
            else:
                upperBound = int(
                    input(
                        f"This integer is smaller than {lowerBound}. Give me a valid integer larger than {lowerBound}:"
                    )
                )
        except ValueError as input_error:
            upperBound = input(
                f"This is not a valid integer. Give me a valid integer larger than {lowerBound}:"
            )

    print(f"OK then, a number between {lowerBound} and {upperBound} ?")

    actualNumber = random.randint(
        lowerBound, upperBound
    )  # generates random number between 0 and upper bound

    guessed = False  # a variable is made which is used later in the loop

    while not guessed:  # starts a loop which starts everytime guessed = False
        try:
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
            elif guessedNumber >= upperBound or guessedNumber <= lowerBound:
                print(
                    f"READ THE QUESTION BRO! Guess a number BETWEEN {lowerBound} and {upperBound}:"
                )
            elif (
                guessedNumber < actualNumber
            ):  # if the guessed number is less than the actual number, it will tell it is too small
                print("Too small, try again :'(")
            elif guessedNumber > actualNumber:
                print("Too big, try again :'(")
        except ValueError as input_error:
            print(
                f"This is not a valid integer. Guess a valid integer between {lowerBound} and {upperBound}."
            )
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
