"""IO examples.

Using file IO, from the docs:
    "The first argument is a string containing the filename. The second
    argument is another string containing a few characters describing the
    way in which the file will be used. 
    mode can be
    'r' when the file will only be read,
    'w' for only writing (an existing file with the same name will be erased),
    and 'a' opens the file for appending; any data written to the file is automatically added to the end.
    'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be
    assumed if it's omitted."
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

"""

import json


def be_cool(name):
    """Just print, not actually doing any IO."""
    print(f"{name} is cool")


be_cool("Ben")


def be_cool_for_ever(name, file_path):
    """Save a message about being cool for ever."""
    mode = "w"  # from the docs
    history_book = open(
        file_path, mode
    )  # opens the file specified in file_path in the specified mode
    history_book.write(
        f"{name} is cool"
    )  # writes the string "{name} is cool" to the file
    history_book.close()  # closes the file to ensure all data is written and resources are freed.


# look up what '..' means
be_cool_for_ever(
    "Ben", "../ben_is_cool.txt"
)  # runs the function, creates a txt file in the parent directory of the current one and writes Ben is cool.
be_cool_for_ever(
    "Ben", "ben_is_cool.lol_UR_joking"
)  # same thing but creates a file called ben_is_cool.lol_UR_joking


def safely_write(name, file_path):
    with open(
        file_path, "w", encoding="utf-8"
    ) as history_book:  # opens the file specified by file_path in write mode with UTF-8 encoding.
        # The with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.
        history_book.write(
            f"{name} is cool 💩💩"
        )  # writes the string "{name} is cool 💩💩" to the file.


safely_write(
    "🕺👆☝🦆", "ducks.yes"
)  # write the string "🕺👆☝🦆 is cool 💩💩" to the file named ducks.yes.

# See where each file was saved


def who_is_cool(file_path):
    """Read a file and print what it says."""
    mode = "r"  # from the docs
    history_book = open(file_path, mode)
    response = history_book.read()
    message = "historians have recorded that:\n\t"
    print(message + response)
    history_book.close()


who_is_cool("../ben_is_cool.txt")
# Open the file ../ben_is_cool.txt in read mode.
# Read the contents of the file into the response variable.
# Create a message: "historians have recorded that:\n\t".
# Print the message followed by the contents of the file.
# Close the file.
who_is_cool("Set4/lazyduck.json")


# some JSON examples:


def bury_time_capsule(
    something_for_your_kids_to_find, file_path
):  # save a dictionary as a JSON file
    """Save some json to a file.

    Args:
        something_for_your_kids_to_find (dict): A dictionary of facts.
        file_path (str): The path to where you want to save the json.
    """
    try:
        dumped = json.dumps(
            something_for_your_kids_to_find
        )  # converts the dictionary into a JSON-formatted string and assigns it to the variable dumped.
        mode = "w"  # from the docs
        time_capsule = open(
            file_path, mode
        )  # opens the file specified by file_path in mode and assigns the file object to the variable time_capsule.
        time_capsule.write(dumped)  # writes the JSON string dumped to the file.
        time_capsule.close()
        return True
    except Exception as e:
        print(e)
        return False


message_for_capsule = {
    "name": "Ben",
    "Year": 2019,
    "Location": "Sydney",
    "Greeting": "Yo whatup now and give a brother room",
    "Fact": "It would take 1,200,000 mosquitoes, each "
    + "sucking once, to completely drain the "
    + "average human of blood",
    "Alphabet Inc Class A": "1106.50USD",
    "fruit": ["apple", "apricot", "avocado", "abiu"],
}

bury_time_capsule(message_for_capsule, "under_the_patio.json")


def dig_up_capsule(file_path):
    """Read some json from a file.

    Does some defensive programming as an example of how you'd do such a thing.
    Args:
        file_path (str): The path to where you want to save the json.
    """
    mode = "r"  # from the docs
    template = """{Greeting},\nDid you know that in {Year}, "{Fact}" was still true!"""
    keys_needed = ["Greeting", "Year", "Fact"]
    try:
        time_capsule = open(file_path, mode)
        contents = json.load(time_capsule)
        time_capsule.close()
        if all([key in contents for key in keys_needed]):
            print(template.format(**contents))
            return True
        else:
            print("Your dictionary is missing some keys.", contents, keys_needed)
            return False
    except Exception as e:
        print(e)
        return False


dig_up_capsule("under_the_patio.json")
