import string
from typing import List

import enchant

alphabet = set(string.ascii_lowercase)


def word_contains(word: str, necessary: str) -> bool:
    """Check if a word contains all of the given characters

    :param word: the word to check
    :param necessary: a string containing all necessary characters ("" for none)
    :return: True if the word contains all characters
    """
    characters = set(necessary)
    for ch in characters:
        if ch not in word:
            return False
    return True


def get_words(excluded: str, necessary: str, char1: str, char2: str, char3: str, char4: str, char5: str) -> List[str]:
    """Get all english words matching the given constraints

    :param excluded: a string containing all excluded characters
    :param necessary: a string containing all necessary characters
    :param char1: character at position 1 ("" for any)
    :param char2: character at position 2 ("" for any)
    :param char3: character at position 3 ("" for any)
    :param char4: character at position 4 ("" for any)
    :param char5: character at position 5 ("" for any)
    :return: a list of all 5-letter words matching the given constraints
    """
    dictionary = enchant.Dict("en_US")

    choices = alphabet - set(excluded)
    choices1 = char1 if len(char1) == 1 else choices
    choices2 = char2 if len(char2) == 1 else choices
    choices3 = char3 if len(char3) == 1 else choices
    choices4 = char4 if len(char4) == 1 else choices
    choices5 = char5 if len(char5) == 1 else choices

    results = []
    for c1 in choices1:
        for c2 in choices2:
            for c3 in choices3:
                for c4 in choices4:
                    for c5 in choices5:
                        word = c1 + c2 + c3 + c4 + c5
                        # would it maybe be more efficient to not generate words that don't contain all necessary
                        # characters? if so: how to keep it simple and readable?
                        if dictionary.check(word) and word_contains(word, necessary):
                            results.append(word)

    return results


def main() -> None:
    excluded = input("Please enter all excluded characters: ").strip().lower()

    necessary = input("Please enter all necessary characters: ").strip().lower()

    # TODO refactor this and the following inputs and re-ask for input if the input contains anything other then
    # a single character
    c1 = input("Character at position 1 (press Enter for any): ").strip().lower()
    char1 = c1 if (len(c1) == 1) and (c1 in alphabet) else ""

    c2 = input("Character at position 2 (press Enter for any): ").strip().lower()
    char2 = c2 if (len(c2) == 1) and (c2 in alphabet) else ""

    c3 = input("Character at position 3 (press Enter for any): ").strip().lower()
    char3 = c3 if (len(c3) == 1) and (c3 in alphabet) else ""

    c4 = input("Character at position 4 (press Enter for any): ").strip().lower()
    char4 = c4 if (len(c4) == 1) and (c4 in alphabet) else ""

    c5 = input("Character at position 5 (press Enter for any): ").strip().lower()
    char5 = c5 if (len(c5) == 1) and (c5 in alphabet) else ""

    solutions = get_words(excluded, necessary, char1, char2, char3, char4, char5)
    print(f"Possible solutions: {solutions}")


if __name__ == '__main__':
    main()
