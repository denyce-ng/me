"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#this is a list of strings
some_words = ["what", "does", "this", "line", "do", "?"]

#I think the function will print the first string in the list some_words
for word in some_words:
    print(word) #the function printed every string in the list
#I think the function will print the first string in the list some_words

for x in some_words:
    print(x) #the function printed every string in the list

#I think this function will print the whole list
print(some_words) #the function printed the WHOLE list including the brackets, the commas and the quotes

#if there are more than 3 items in the list some_words, it will print "some_words contains more than 3 words"
if len(some_words) > 3:
    print("some_words contains more than 3 words") #if there are more than 3 objects in the list some_words then it will print "some_words contain more than 3 words" 

#uname provides system information
#the function will print system information of the platform it is run on
def usefulFunction():
    """
    You may want to look up what uname does before you guess 
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) #the function prints the system information of the device


usefulFunction()
