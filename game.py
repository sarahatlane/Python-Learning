
# python number_guessing_game


# generate a random number between 1 and 100:

import random

secret_number = random.randint(1, 100)


# Get User Input:

guess = int(input("Enter your guess (between 1 and 100): "))


# Check Guess:
# Compare the player's guess with the secret number and provide feedback
# If the guess is correct, end the game
# Otherwise, provide hints to help the player guess the number


if guess == secret_number:
    print("Congratulations! You guessed the number.")
elif guess < secret_number:
    print("Too low! Try guessing a higher number.")
else:
    print("Too high! Try guessing a lower number.")



# Repeat or End Game:
# Allow the player to make multiple guesses until they guess the correct number or reach a maximum number of attempts.
# using a loop (e.g., while loop) to achieve this:
    
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Enter your guess (between 1 and 100): "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low! Try guessing a higher number.")
    else:
        print("Too high! Try guessing a lower number.")

if attempts == max_attempts:
    print("Sorry, you've run out of attempts. The correct number was", secret_number)
# --------------------------------------------------------------------------------------------------------------------------------------------------



import random

secret_number = random.randint(1, 100)
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    guess = int(input("Enter your guess (between 1 and 100): "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low! Try guessing a higher number.")
    else:
        print("Too high! Try guessing a lower number.")

if attempts == max_attempts:
    print("Sorry, you've run out of attempts. The correct number was", secret_number)

