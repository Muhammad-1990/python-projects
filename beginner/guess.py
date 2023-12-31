# A simple game to guess a random number

# Import the random module
import random

# Print a welcome message
print("Welcome to the Guess the Number Game!")

def guess(x):
    # Generate a random number between 1 and x
    random_number = random.randint(1, x)

    # Ask the user to guess the number
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        # Print a message if the guess is too high or too low
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    # Print a message if the guess is correct
    print(f"Yay, congrats. You have guessed the number {random_number} correctly!")

# Call the function
guess(int(input("Enter the maximum number:")))

# End of program