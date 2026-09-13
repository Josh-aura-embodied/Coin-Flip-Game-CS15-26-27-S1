import random


def main():
    print("Welcome to the Coin Flip Game!")
    print("Guess 'heads' or 'tails'.")
    print("Twist: The game ends if you make 3 incorrect guesses in a row!\n")

    consecutive_incorrect = 0
    rounds_played = 0

    # The game continues as long as the player hasn't hit 3 strikes
    while consecutive_incorrect < 3:
        rounds_played += 1
        print(f"--- Round {rounds_played} ---")

        # 1. Validate the player's input
        valid_input = False
        while not valid_input:
            guess = input("What is your guess? (heads/tails): ").lower().strip()
            if guess == "heads" or guess == "tails":
                valid_input = True
            else:
                print("Invalid input. Please type 'heads' or 'tails'.")

        # 2. Randomly determine the coin flip
        coin = random.choice(["heads", "tails"])
        print(f"The coin landed on... {coin}!")

        # 3. Check the result and update the twist mechanics
        if guess == coin:
            print("Correct!")
            # A correct guess resets the incorrect-guess counter to 0
            consecutive_incorrect = 0
        else:
            print("Incorrect!")
            # Add to the strike counter
            consecutive_incorrect += 1

            # 4. Display the needed information for the chosen twist
        print(f"Strikes (Consecutive Incorrect Guesses): {consecutive_incorrect}/3\n")

    print(f"Game Over! You made 3 incorrect guesses in a row.")
    print(f"You survived for {rounds_played - 1} rounds.")


if __name__ == "__main__":
    main()