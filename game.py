# game.py

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of'rock','paper','scissors':")
print("USER CHOICE: ", user_choice)

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("Valid, keep going")
else:
    print("invalid input")
exit()

print("This is the end of our game, please play again.")