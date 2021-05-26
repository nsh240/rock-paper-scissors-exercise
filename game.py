# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of'rock','paper','scissors':")
print("USER CHOICE: ", user_choice)

if (user_choice != "rock") or (user_choice != "paper") or (user_choice != "scissors"):
    print("Valid, keep going")
else:
    print("invalid input")
    exit()

valid_options=["rock","paper","scissors"]
computer_choice = random.choice(valid_options)
print("Computer choice: ", computer_choice)

if user_choice==computer_choice:
    print("tie")
if user_choice=="rock" and computer_choice=="scissors":
    print("The User wins")
if computer_choice=="rock" and user_choice=="scissors":
    print("The Computer wins")


print("This is the end of our game, please play again.")