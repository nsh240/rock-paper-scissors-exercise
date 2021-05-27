# game.py

import random
import os
from dotenv import load_dotenv
load_dotenv()


user_name = os.environ["PLAYER_NAME"]
# print("Welcome ", user_name)

#refactored with concatenation:
print("Welcome "+ user_name)

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

# if user_choice==computer_choice:
#     print("It's a Tie.")
# elif user_choice=="rock" and computer_choice=="scissors":
#     print("The User wins")
# elif computer_choice=="rock" and user_choice=="scissors":
#     print("The Computer wins")
# elif user_choice=="paper" and computer_choice=="rock":
#     print("The User wins")
# elif computer_choice=="paper" and user_choice=="rock":
#     print("The Computer wins")
# elif user_choice=="scissors" and computer_choice=="paper":
#     print("The User wins")
# elif computer_choice=="scissors" and user_choice=="paper":
#     print("The Computer wins")

#refactored below

if user_choice== "rock":
    if computer_choice=="paper":
        print("The Computer Wins")
    elif computer_choice=="scissors":
        print("The User Wins")

if user_choice=="paper":
    if computer_choice=="rock":
        print("The User Wins")
    elif computer_choice=="scissors":
        print("The Computer Wins")

if user_choice=="scissors":
    if computer_choice=="rock":
        print("The Computer Wins")
    if computer_choice=="paper":
        print("The User Wins")

print("This is the end of our game, please play again.")



