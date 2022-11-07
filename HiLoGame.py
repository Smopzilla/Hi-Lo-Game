#!/usr/bin/env python
# Peri
# 2021.11.14
# Lab Exercise 5
# Calculator.py
# Using Mu 1.1.0.beta.6
# Generates a number that the user must guess and
# confirms or denies the guess and reprompts the
# user until the guess is correct.

# Import random and sys module
import random
import sys

# Use a while loop to re-prompt
while True:
    try:
        # Ask user for a max number
        max_num = int(input("What should the maximum number for this game be? "))
        # Check if number is higher than 1
        if max_num <= 1:
            print("Enter a number higher than 1!")
        else:
            # Generate a number within range
            comp_num = random.randint(1, max_num)
            break
    except ValueError:
        # Catch an error
        print("Enter a non-floating number only!")
        continue

# Use a while loop to re-prompt
while True:
    try:
        # Ask user for a guess
        guess = int(input("Guess my number: "))
        # Check if number is higher than 1
        if guess < 1:
            print("Enter a number equal to or higher than 1!")
        else:
            # Check if number is a match
            if comp_num == guess:
                print("You guessed my number!")
                # Use a while loop to re-prompt
                while True:
                    # Ask if user wants to play again
                    again = input("Do you want to play again? Y/N ")
                    # Check if answer is valid
                    if again.lower() in("y", "n", "yes", "no"):
                        if again.lower() in("n", "no"):
                            # End the program
                            sys.exit("Thank you for playing!")
                        else:
                            break
            # Check if guess is higher than range
            elif guess > max_num:
                print("Choose a number lower than", str(max_num) + "!")
                continue
            # Check if guess is too high
            elif comp_num < guess:
                print("Your guess is too high.")
                continue
            # Check if guess is low
            elif comp_num > guess:
                print("Your guess is too low.")
                continue
    except ValueError:
        # Catch an error
        print("Enter a non-floating number only!")
        continue
    else:
        # Use a while loop to re-prompt
        while True:
            try:
                # Ask user for a max number
                max_num = int(input("What should the maximum number for this game be? "))
                # Check if number is higher than 1
                if max_num <= 1:
                    print("Enter a number higher than 1!")
                else:
                    # Generate a number within range
                    comp_num = random.randint(1, max_num)
                    break
            except ValueError:
                # Catch an error
                print("Enter a non-floating number only!")
                continue