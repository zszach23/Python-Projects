# Number Guessing Game
# Zach Sally
# Topics - Random Number Generation, Type Casting, Iteration, Import Libraries

from curses.ascii import isdigit
import random

top_of_range = input("Type a number: ")

# Check user input number
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    quit()

# Initialize random number to be between 1 and input
random_number = random.randint(1, top_of_range)
attempts = 0

# Loop
while True:

    # Check input guess for validity
    guess = input("Guess a number between 1 and " + str(top_of_range) + ": ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number next time")
        continue

    attempts += 1

    # Check input guess for accuracy
    if guess == random_number:
        break
    elif guess < random_number:
        print("Your guess was too low")
    else:
        print("Your guess was too high")

# Display number of attempts
print("You guessed the number!")
print("It took you", attempts, "tries")