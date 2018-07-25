from itertools import permutations


def find_anagrams(word, word_list):
    """Finds all valid anagrams for a given word.

    Args:
        word (str): the word we want to find anagrams for
        word_list (list): a list of valid words in the english language

    Returns:
        set: a set of valid anagrams of the given word
    """
    # warn for the length of execution
    # = cheap conversational hack-around... :P
    if len(word) > 7:
        print("choose a shorter word (or wait...)")
    elif len(word) > 6:
        print("this might take a while...")

    # long thing that does what it shalls - but inefficiently!!
    anagrams = {''.join(w) for w in permutations(word, len(word))
                if ''.join(w) in word_list}
    return anagrams

# fetching our list of acceptable words
with open('words.txt', 'r') as fin:
    word_list = fin.readlines()
    word_list = [w.rstrip() for w in word_list]

if __name__ == '__main__':
    while True:
        word = input("Enter a word to find its anagrams: ")
        print(find_anagrams(word, word_list))
