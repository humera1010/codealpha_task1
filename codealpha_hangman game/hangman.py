import random

words = ["planet", "python", "forest", "camera", "rocket"]

secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("================================")
print("      HANGMAN WORD GAME")
print("================================")

while wrong_guesses < max_attempts:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        remaining = max_attempts - wrong_guesses
        print("Wrong guess!")
        print("Attempts left:", remaining)

else:
    print("\nGame Over!")
    print("The word was:", secret_word)