"""A number-guessing game."""

# Put your code here
import random
"""A number-guessing game."""

# Put your code here
name = input('Hello, please enter your name ')
guess = None

random_num = random.randint(1, 100)
guesses = 0

while guess != random_num:
  guess = int(input('Please guess a number between 1-100 '))
  guesses += 1
  if guess == random_num:
    print(f'You guessed the number! It took you {guesses} tries.')
  elif guess < random_num:
    print(f'{guess} is too low. ')
  elif guess > random_num:
    print(f'{guess} is too high. ')
