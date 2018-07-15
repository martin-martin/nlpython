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
