TODO: Reflect on what you learned this week and what is still unclear.

The input("Enter your name: ") function displays the message "Enter your name: " and waits for the user to type their name.
so input("prompt") requires the user to input something according to prompt

ELIF VS ELSE
elif is used to check additional conditions after an if statement.
else is used as the final option when none of the preceding conditions are True

When Python encounters the break statement, it immediately exits the loop it's currently in, regardless of the loop's condition.

the try...except block is used to handle errors or exceptions that may occur during the execution of code
When an error is gotten then
eg:
try:
smtg smtg (any line of code you want to execute but also want to check for any errors in except)
except <error name> as <variable>: #this sets variable as error message (predetermined):
what you want to do if <error name> is detected

while true: infinite loops
while <condition>: loop that will carry out every time <condition> is met.
while not <condition>: loop that will carry out ever time <condition> is NOT met.

\n: The \n in the print statement print("\nWelcome to the guessing game!") is a special escape sequence in Python called a "newline character." When Python encounters \n within a string, it interprets it as a newline character, which causes the text following it to be printed on a new line.

the pseudocode for binary search, modified for searching in an array.
The inputs are the array, which we call array; the number n of elements in array; and target, the number being searched for. The output is the index in array of target:
Let min = 0 and max = n-1.
Compute guess as the average of max and min, rounded down (so that it is an integer).
If array[guess] equals target, then stop. You found it! Return guess.
If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
Otherwise, the guess was too high. Set max = guess - 1.
Go back to step 2.
