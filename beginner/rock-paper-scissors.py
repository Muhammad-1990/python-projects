# A simple user vs computer rock paper scissors game

import random

# Define the game options
options = ["rock", "paper", "scissors"]

# Define the game rules
rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

# Define the game results
results = {
    "win": "You win!",
    "lose": "You lose!",
    "draw": "It's a draw!"
}

# Define the game loop
while True:
    # Get the user's choice
    user_choice = input("Rock, paper or scissors? ").lower()

    # Check if the user's choice is valid
    if user_choice not in options:
        print("Invalid choice!")
        continue

    # Get the computer's choice
    computer_choice = random.choice(options)

    # Check the result
    if user_choice == computer_choice:
        result = "draw"
    elif rules[user_choice] == computer_choice:
        result = "win"
    else:
        result = "lose"

    # Print the result
    print(f"You chose {user_choice}, computer chose {computer_choice}. {results[result]}")

    # Ask the user if they want to play again
    play_again = input("Play again? (y/n) ").lower()

    # Check if the user wants to play again
    if play_again != "y":
        break