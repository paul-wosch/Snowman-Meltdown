"""Provide game logic for the snowman guessing game."""
import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the game state as ASCII art."""
    # Display the snowman stage for the current number of mistakes.
    print(ascii_art.STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    """Run the game logic."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    # Prompt the user until they win or exceed mistake limit
    while mistakes < 3:
        # Display the game state.
        display_game_state(mistakes, secret_word, guessed_letters)
        while True:
            guess = input("Guess a letter: ").lower().strip()
            if len(guess) == 1 and guess.isalpha():
                break
            print("Invalid input! Only single letter is allowed.")
        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1

        if sorted(list(set(guessed_letters))) == sorted(list(secret_word)):
            print("Congratulations, you saved the snowman!")
            break
        if mistakes == 3:
            print(f"Game Over! The word was: {secret_word}")
