"""
computer picks a random number between 1-10
user guesses number until it is correct

example:
user: 1
Try again!
3
Correct!

flow:
generate the random number between 1-10
user input with the guess
if statement

improvements:
if you don't put in a guess, show what the guess was
"""

import random


DEFAULT_GUESS = 0
DEFAULT_RANGE = 10


max_range = int(input('Guess between 1 and...? (default: 10)\t') or DEFAULT_RANGE)
if max_range < 1:
    max_range = DEFAULT_RANGE

number = random.randint(1, max_range)

guess = int(input(f'Guess my number between 1 and {max_range}!\t') or DEFAULT_GUESS)
if guess != DEFAULT_GUESS:
    while guess != number:
        guess = int(input('Nope, try again!\t') or DEFAULT_GUESS)
    print("Good job!")
else:
    print(f'The number was: {number}')
