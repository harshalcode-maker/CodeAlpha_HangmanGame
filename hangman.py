
import random

# List of 5 predefined words
words = ["python", "computer", "program", "developer", "keyboard"]

# Select a random word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses allowed.")
print("Type 'hint' to reveal a random letter.\n")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display current word progress
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_attempts)

    # Check if player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word!")
        break

    # Take user input
    guess = input("Enter a letter or type 'hint': ").lower()

    # Hint system
    if guess == "hint":

        hidden_letters = [
            letter for letter in secret_word
            if letter not in guessed_letters
        ]

        if hidden_letters:
            hint_letter = random.choice(hidden_letters)
            guessed_letters.append(hint_letter)
            print("Hint! The letter revealed is:", hint_letter)
        else:
            print("No hidden letters left!")

        continue

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter!")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Game over condition
if incorrect_guesses == max_attempts:
    print("\nGame Over! You lost.")
    print("The correct word was:", secret_word)

# Final message
print("\nThanks for playing Hangman!")
