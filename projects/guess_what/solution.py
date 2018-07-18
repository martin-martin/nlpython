'''
Build a command-line game that prompts a player to guess a word.

STEPS:
*) read a word list from a file (e.g. 'words.txt' that is provided)
*) select a random word as the challenge word and print out the number
    of characters as underscores (e.g.: 'hello' would be '_ _ _ _ _')
*) prompt the player to input a character
*) if the character is in the word, mark it and print out the blank word
    with the character inserted (e.g. '_ e _ _ _')
*) if the character is not in the word, decrease a counter of max tries
    that the player has to guess the word
*) if the player guesses all characters before the 'tries' counter
    reaches zero, print a message to congratulate them
*) otherwise end the game and explain the player that they lost

'''

import random


def main():
    word = get_random_word()
    play_game(word)


def get_random_word():
    # read in the file content
    with open('words.txt', 'r') as f:
        data = f.readlines()
        # removing the newline characters at the end of each word
        all_words = [w.rstrip() for w in data]

    # pick a random word
    # and transform to a list of characters for easier handling
    word = list(random.choice(all_words))
    return word


def play_game(word):

    blank = list('_' * len(word))
    print(f"Your challenge: {' '.join(blank)}")

    tries = 10
    while '_' in blank:
        if tries <= 0:
            break

        guess = input("Guess a letter: ")
        # guess = "s"
        tries -= 1

        if guess in word:
            for i, c in enumerate(word):
                if guess == c:
                    blank[i] = c

            print(f"Nice! Keep going: {' '.join(blank)}")

        else:
            print("Nope. Sorry, try again.")
        print(f"{tries} tries left...")

    if '_' not in blank:
        print("You won! Peaches!")
    else:
        print("Whoops, sorry - outta tries... Bye!")
        print(f"Your nemesis was: {''.join(word)}")


if __name__ == '__main__':
    main()
