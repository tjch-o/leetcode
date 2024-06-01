def get_char_freq(s):
    result = {}

    for c in s:
        result[c] = result.get(c, 0) + 1
    return result


def is_anagram(s, t):
    return get_char_freq(s) == get_char_freq(t)
