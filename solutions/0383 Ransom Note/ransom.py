def get_frequency_list(s):
    result = {}

    for c in s:
        result[c] = result.get(c, 0) + 1
    return result


def can_construct(ransomNote, magazine):
    magazine_freq = get_frequency_list(magazine)

    for c in ransomNote:
        if c not in magazine_freq:
            return False
        magazine_freq[c] -= 1

        if magazine_freq[c] == 0:
            del magazine_freq[c]
    return True
