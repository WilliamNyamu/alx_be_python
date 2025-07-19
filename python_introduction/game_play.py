# Import the random module so we can generate random numbers
import random

# Start the game loop
play_again = "yes"

while play_again.lower() == "yes":
    # Generate a secret number between 1 and 10
    secret_number = random.randint(1, 10)

    # Counter to track number of guesses
    guess_count = 0

    # Let the user keep guessing until they get it right
    while True:
        # Ask the user to guess the number
        guess = int(input("Guess a number between 1 and 10: "))
        guess_count += 1  # Increase the guess count

        # Use match-case to check the guess
        match guess:
            case x if x == secret_number:
                print(f"🎉 Congratulations, you guessed it!")
                print(f"You took {guess_count} guesses.")
                break  # Exit the inner loop
            case x if x > secret_number:
                print("📈 Oops, your guess is a bit high. Try again!")
            case x if x < secret_number:
                print("📉 Nope, your guess is a bit low. Give it another shot!")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")

print("Thanks for playing! Goodbye! 👋")
