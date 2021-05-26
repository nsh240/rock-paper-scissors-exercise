# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of'rock','paper','scissors':")
print("USER CHOICE: ", user_choice)

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("Valid, keep going")
else:
    print("invalid input")
    exit()

valid_options=["rock","paper","scissors"]
computer_choice = random.choice(valid_options)
print("Computer choice: ", computer_choice)

print("This is the end of our game, please play again.")