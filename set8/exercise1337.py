# -*- coding: UTF-8 -*-
"""
I'm in UR exam.
This is the same as the setly exercises, fill in the functions,
and test them to see if they work.
You have 2 hours.
"""
import json
import os
import random
import string
import time
from typing import Any
import requests


def give_me_five() -> int:
    """Returns the integer five."""
    return 5


def password_please() -> str:
    """Returns a string, 8 or more characters long, contains at
    least one upper case letter and one lowercase letter.
    TIP: don't put in a real password!"""
    return "HelloIwillacethis"


def list_please() -> list[Any]:
    """Returns a list, you can put anything in the list."""
    return ["Hello", 8, "No"]


def int_list_please() -> list[int]:
    """Returns a list of integers, any integers are fine."""
    return [5, 7, 9]


def string_list_please() -> list[str]:
    """Returns a list of strings, any string are fine."""
    return ["Hello", "Yes", "True"]


def dictionary_please() -> dict:
    """Returns a dictionary, anything you like."""
    return {"Name": "Ben Doherty", "Reason of Absence": "idk"}


def is_it_5(some_number) -> bool:
    """Returns True if the argument passed is 5, otherwise returns False."""
    well_is_it = None
    if some_number == 5:
        well_is_it = True
    else:
        well_is_it = False
    return well_is_it


def take_five(some_number) -> int:
    """Subtracts 5 from some_number."""
    return some_number - 5


def greet(name="Towering Timmy") -> str:
    """Return a greeting.
    return a string of "Well hello, " and the name argument.
    E.g. if given as "Towering Timmy" it should
         return "Well hello, Towering Timmy"
    """
    return f"Well hello, {name}"


def one_counter(input_list=[1, 4, 1, 5, 1, 1]) -> int:
    """Count the number of 1s in the input_list.
    Return an integer.
    TIP: the test will use a different input_list, so don't just return 2
    """
    count = 0
    for integer in input_list:
        if integer == 1:
            count += 1

    return count


def n_counter(search_for_this, input_list=[1, 4, 1, 5, 1, 1]) -> int:
    """Count the number of times search_for_this shows up in the input_list.
    Return an integer.
    """
    count = 0
    for integer in input_list:
        if integer == search_for_this:
            count += 1
    return count


def fizz_buzz() -> list:
    """Do the fizzBuzz.

    This is the most famous basic programming test of all time!

       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."

    from https://blog.codinghorror.com/why-cant-programmers-program/

    Return a list that has an integer if the number isn't special,
    and a string if it is. E.g.
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
         'Fizz', 'Buzz',  11, 'Fizz', 13, 14,
         'FizzBuzz', 16, 17, ...]
    """
    fizz_buzz_list = []
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            fizz_buzz_list.append("FizzBuzz")
        elif i % 5 == 0:
            fizz_buzz_list.append("Buzz")
        elif i % 3 == 0:
            fizz_buzz_list.append("Fizz")
        else:
            fizz_buzz_list.append(i)

    return fizz_buzz_list


def set_it_on_fire(input_string="very naughty boy") -> str:
    """Interleave the input_string with the 🔥 emoji.

    Given any string, interleave it with 🔥. Also make it be upper case.
    e.g. "very naughty boy" should return the string
    "🔥V🔥E🔥R🔥Y🔥 🔥N🔥A🔥U🔥G🔥H🔥T🔥Y🔥 🔥B🔥O🔥Y🔥"
    TIP: strings are pretty much lists of chars.
         If you list("string") you get ['s', 't', 'r', 'i', 'n', 'g']
    TIP: consider using the 'join' method in Python.
    TIP: make sure that you have a 🔥 on both ends of the string.
    """
    string = list(input_string.upper())
    number_of_characters = len(string)
    character_index = 0
    emoji_list = []
    for i in range(number_of_characters * 2):
        if i == 0:
            emoji_list.append("🔥")
        if i % 2 == 0:
            emoji_list.append(string[character_index])
            character_index += 1
        if i % 2 == 1:
            emoji_list.append("🔥")

    return "".join(emoji_list)


def the_chain_gang_5(the_value) -> bool:
    """Take the_value, subtract 5 from it, and return True if the value we end up with it 5.

    You don't get anything for free this far into the quiz, you can't
    use the == operator or the - operator, and you must use two of the
    functions you've already written.

    TIP: you've already written a function that returns True if the value is 5
    TIP: you've already written a function that subtracts 5
    """

    return is_it_5(take_five(the_value))


def pet_filter(letter="a") -> list:
    """Return a list of pets whose name contains the character 'letter'"""
    # fmt: off
    pets = [
        "dog", "goat", "pig", "sheep", "cattle", "zebu", "cat", "chicken", 
        "guinea pig", "donkey", "duck", "water buffalo", "python", "scorpion",
        "western honey bee", "dromedary camel", "horse", "silkmoth", 
        "pigeon", "goose", "yak", "bactrian camel", "llama", "alpaca", 
        "guineafowl", "ferret", "muscovy duck", "barbary dove", "cichlid",
        "bali cattle", "gayal", "turkey", "goldfish", "rabbit", "koi", 
        "canary", "society finch", "fancy mouse", "siamese fighting fish", 
        "fancy rat and lab rat", "mink", "red fox", "hedgehog", "guppy"
    ]
    # fmt: on
    filtered = []
    for pet in pets:
        if letter in pet:
            filtered.append(pet)
    return filtered


def best_letter_for_pets() -> str:
    """Return the letter that is present at least once in the most pet names.

    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    TIP: use the function you just wrote to help you here!
    TIP: you've seen this before in the pokedex.
    """
    import string

    the_alphabet = string.ascii_lowercase
    the_alphabet = list(the_alphabet)
    alphabet_index = 0
    letter_popularity_number = -1
    while alphabet_index < len(the_alphabet):
        current_letter_list = pet_filter(
            the_alphabet[alphabet_index]
        )  # pet_filter(the_alphabet[alphabet_index]) uses previous function to return a list of animals that has the current alphabet in their name
        if len(current_letter_list) > letter_popularity_number:
            best_letter = the_alphabet[alphabet_index]
            letter_popularity_number = len(current_letter_list)
        alphabet_index += 1

    return best_letter


def make_filler_text_dictionary() -> dict:
    """Make a dictionary of random words filler text.
    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=4
    If we set wordlength=18, we will get something like this:
    >>> url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=18"
    >>> r = requests.get(url)
    >>> r.text # will get you a string, something like this:
    >>> "occipitosphenoidal"

    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g.
    {
        3: ['Seb', 'the', 'yob', "boy"],
        4: ['aaaa', 'bbbb', 'cccc', "ddd"],
        ...
        7: ['aaaaaaa', 'bbbbbbb', 'ccccccc', 'ddddddd']
    }
    Use the API to get the 4 words.

    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 4 words for each)
    TIP: you'll need the requests library

    """
    length = 3
    wd = {}
    while length <= 7:
        no_of_words = 0
        url = f"https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length}"
        list_of_words = []
        while no_of_words < 4:
            r = requests.get(url).text
            for i in range(1):
                list_of_words.append(r)
            no_of_words += 1
        current_dict = {f"{length}": list_of_words}
        wd = {**wd, **current_dict}
        length += 1

    return wd


def random_filler_text(number_of_words=200) -> str:
    """Make a paragraph of random filler text.
    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the words.
    Make the paragraph have number_of_words words in it.
    Return it as a string
    TIP: you'll need the random library,
        e.g. random.randint(low, high)
    """

    my_dict = make_filler_text_dictionary()
    words = []
    for i in range(number_of_words):
        random_key = str(random.randint(3, 7))
        random_index = random.randint(0, 3)
        words.append(my_dict[random_key][random_index])

    return " ".join(words)


def fast_filler(number_of_words=200) -> str:
    """Makes filler text, but really fast.

    This time, the first time the code runs, save the dictionary returned
    from make_filler_text_dictionary to a file.
    On the second run, if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_cache.json"
    TIP: you'll need the os and json libraries
    TIP: This is making sentences. Make the first letter capital, and add a full stop to the end.
    TIP: you'll probably want to use json dumps and loads to get the
    dictionary into and out of the file. Be careful when you read it back in,
    it'll convert integer keys to strings.
    If you get this one to work, you are a Very Good Programmer™!
    """
    words = []
    if os.path.isfile("./set8/dict_cache.json"):
        file = open("./set8/dict_cache.json", "r")
        my_dict = json.load(file)
        for i in range(number_of_words):
            random_key = str(random.randint(3, 7))
            random_index = random.randint(0, 3)
            words.append(my_dict[random_key][random_index])
    else:
        my_dict = make_filler_text_dictionary()
        with open("./set8/dict_cache.json", "w") as file:
            json.dump(my_dict, file, indent=4)
    if words:
        first_word = words[0]
        first_word_list = list(first_word)
        first_word_list[0] = first_word_list[0].upper()
        words[0] = "".join(first_word_list)
    para_without_fullstop = " ".join(words)
    if not para_without_fullstop.endswith("."):
        para_without_fullstop += "."
    return para_without_fullstop


if __name__ == "__main__":
    print("give_me_five", give_me_five(), type(give_me_five()))
    print(
        "strong_password_please",
        password_please(),
        type(password_please()) == str,
    )
    print("int_list_please", int_list_please(), type(int_list_please()) == list)
    print(
        "string_list_please", string_list_please(), type(string_list_please()) == list
    )
    print("dictionary_please", type(dictionary_please()) == dict)
    print("is_it_5", is_it_5(5))
    print("is_it_5", is_it_5(6))
    print("take_five", take_five(5))
    print("take_five", take_five(3))
    print("greet:", greet())
    print("three_counter:", one_counter())
    print("n_counter:", n_counter(7))
    print("fizz_buzz:", fizz_buzz())
    print("put_behind_bars:", set_it_on_fire())
    print("chaing gang 5", the_chain_gang_5(5))
    print("chaing gang 5", the_chain_gang_5(10))
    print("pet_filter:", pet_filter())
    print("best_letter_for_pets:", best_letter_for_pets())
    print("make_filler_text_dictionary:", make_filler_text_dictionary())
    print("random_filler_text:", random_filler_text())
    print("fast_filler:", fast_filler())
    for i in range(4):
        print(i, fast_filler(number_of_words=20), "\n")
    print(
        "These are mini tests, they show you some output.",
        "\nDon't forget to run the real tests.",
        "\nThey test your code against the non-default arguments",
    )
