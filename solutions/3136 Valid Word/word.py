def is_valid(word):
    if len(word) < 3:
        return False

    vowels = {"a", "e", "i", "o", "u"}
    has_vowel = False
    has_consonant = False

    for c in word:
        if c.isalnum():
            if c.isdigit():
                continue
            elif c.lower() in vowels:
                has_vowel = True
            else:
                has_consonant = True
        else:
            return False
    return has_vowel and has_consonant
