#!/usr/bin/env python3
# coding=utf-8

"""
The game begins with the computer generating a random integer between 1 and 100. The user will guess a number, and the computer will indicate whether the guess is too high, too low, or correct. This will continue until the user has correctly guessed the computer's number.

use python3 to run it.
"""

import random

def high_low():
  

  #random number generator between 1,100
  #1 and 100 are included in random.randint(1,100)
  #https://docs.python.org/3.1/library/random.html#random.randint
  val = random.randint(1, 100)
  count = 0

  print("I'm thinking of a number between 1 and 100. Guess a number, and I'll tell you if you're too high, too low, or got it right.\n\nGood luck!")

  while True:
    #initialization and increments each loop
    count += 1

    #begins with prompting for a guess
    guess = int(input('\n%s)Please enter a number between 1 and 100:\n ' % count))

    #Code checks for ==, < and > cases
    if guess == val:
      #Concludes with a summary
      print('\nCorrect!\n','It took %s turns.' % count)
      break
    elif guess > val:
      msg = 'Too high!'
    else:
      msg = 'Too low!'

    #Prompt informs user
    print('{}  Try again!'.format(msg))
  return 0


if __name__ == "__main__":
    high_low()
