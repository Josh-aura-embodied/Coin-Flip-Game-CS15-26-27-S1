import random

# PROGRAM START
while True:
    # Randomly choose between heads and tails
    coin = random.choice(["heads", "tails"])

    # Input validation loop to ensure the user types a valid option
    while True:
        guess = input("What is your guess?\n")
        guess = guess.lower()  # Convert to lowercase to make it case-insensitive

        if guess == "heads" or guess == "tails":
            break  # Exit the validation loop if the input is valid
        else:
            print("Invalid input.")

    # Check if the user guessed correctly
    if guess == coin:
        print("Correct!")
    else:
        print("Incorrect!")