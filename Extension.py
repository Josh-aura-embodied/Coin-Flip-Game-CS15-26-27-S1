#STILL WORKING ON IT NEEDS TO BE REDONE
import random


def main():
    strikes = 0

    print("Heads or Tails")
    print("3 wrong guesses in a row and you're out.")
    print()

    while strikes < 3:
        while True:
            guess = input("Heads or tails? ").strip().lower()
            if guess in ["heads", "tails"]:
                break
            print("Just enter heads or tails.")

        coin = random.choice(["heads", "tails"])
        print(f"Landed on {coin}.")

        if guess == coin:
            print("Nice, caught it.")
            strikes = 0
        else:
            strikes += 1
            print("Missed it.")

        print(f"Strikes: {strikes}/3")
        print()

    print("That's 3 strikes in a row. Game over.")


if __name__ == "__main__":
    main()

    