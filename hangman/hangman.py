import random


def get_word():
    # Picks a random word from a list of words and returns it
    words = ["python", "java", "javascript", "php"]
    word = random.choice(words)
    return word.lower()


def play():
    # Implements the gameplay of the game "Hanger"
    word = get_word()

    word_completion = "_" * len(word)
    guessed_letters = []
    tries = 8

    print("Let's play Hangman!")
    print(word_completion)

    while tries > 0:
        guess = input("Please guess a lowercase English letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed this letter.")
            continue

        if len(guess) != 1:
            print("You should input a single letter.")
            continue

        if not guess.isalpha():
            print("Please enter a lowercase English letter.")
            continue

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    word_completion = word_completion[:i] + guess + word_completion[i + 1:]
            print(word_completion)

            if "_" not in word_completion:
                print("Congratulations, you guessed the word!")
                break
        else:
            print("That letter doesn't appear in the word.")
            print(word_completion)

    if tries == 0:
        print("Sorry, you ran out of tries. The word was", word)


def main():
    # The main() function is responsible for starting the game and displaying the menu
    while True:
        print("Type \"play\" to play the game, \"exit\" to quit:")
        choice = input()
        if choice == "play":
            play()
        elif choice == "exit":
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
