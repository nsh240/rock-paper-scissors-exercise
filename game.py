# game.py

import random

#print("Rock, Paper, Scissors, Shoot!")
print("Welcome Player One!")

user_choice = input("Please choose one of'rock','paper','scissors':")
print("User choice: ", user_choice)

if (user_choice == "rock") or (user_choice == "paper") or (user_choice== "scissors"):
    message="good"
else:
    print("Invalid Input. Please enter 'rock','paper', or 'scissors'")
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
if user_choice=="paper" and computer_choice=="rock":
    print("The User wins")
if computer_choice=="paper" and user_choice=="rock":
    print("The Computer wins")
if user_choice=="scissors" and computer_choice=="paper":
    print("The User wins")
if computer_choice=="scissors" and user_choice=="paper":
    print("The Computer wins")


#
# A friendly welcome message, including the player's name (by default, use "Player One").
# The user's selected option
# The computer's selected option
# Whether the user or the computer was the winner
# A friendly farewell message


print("This is the end of our game, please play again.")



