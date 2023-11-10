import random

print("Welcome to Hangman!")
print("Instructions:\n 1. Guess the letters of the word one by one\n 2.Total No. of guesses = 6, within that you have to find the answer\n 3. If the letter isn't in the word then a body part will be added to the gallows (head, body, left arm, right arm, left leg, right leg) ")

count=6
# List of words for the game
word_list = ["python", "hangman", "computer", "programming", "challenge", "gaming"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to display the hangman figure
def display_hangman(incorrect_guesses):
    hangman_figures = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |"
    ]
    return hangman_figures[incorrect_guesses]

# Main game loop
while True:
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_guesses = 0

    while True:
        print(display_hangman(incorrect_guesses))
        print(display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            if all(letter in guessed_letters for letter in word_to_guess):
                print("Congratulations! You guessed the word:", word_to_guess)
                break

        else:
            guessed_letters.append(guess)
            incorrect_guesses += 1
            count -=1
            print("Nah!, Remaining Guesses:", count)

        if incorrect_guesses == 6:
            print("Sorry, you've run out of guesses. The word was:", word_to_guess)
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
