def is_consonant(c):
    return not is_vowel(c) and c.isalpha()


def is_vowel(c):
    return c in ["a", "e", "i", "o", "u"] and c.isalpha()


def is_valid(word):
    if len(word) <= 2:
        return False

    word = word.lower()
    has_vowel = False
    has_consonant = False

    for c in word:
        if is_vowel(c):
            has_vowel = True
        elif is_consonant(c):
            has_consonant = True
        elif not c.isdigit():
            return False
    return has_consonant and has_vowel
