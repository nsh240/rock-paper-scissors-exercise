# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of'rock','paper','scissors':")
print("USER CHOICE: ", user_choice)

if (user_choice == "rock") or (user_choice == "paper") or (user_choice== "scissors"):
    message="good"
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



# The application should compare the user's selection to the computer player's selection, and determine which is the winner. The following logic should govern that determination:

# Rock beats Scissors
# Paper beats Rock
# Scissors beats Paper
# Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

# After determining the winner, the application should display the results to the user. Desired information outputs (from start to finish) should include at least the following:

# A friendly welcome message, including the player's name (by default, use "Player One").
# The user's selected option
# The computer's selected option
# Whether the user or the computer was the winner
# A friendly farewell message


print("This is the end of our game, please play again.")



