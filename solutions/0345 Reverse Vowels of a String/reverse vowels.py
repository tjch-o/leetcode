def replace_string(s, i, char):
    return s[:i] + char + s[i + 1 :]


def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    n = len(s)
    vowels_present = []
    output = s

    if n == 1:
        return s

    for char in s:
        if char in vowels:
            vowels_present.append(char)

    for i in range(n):
        if s[i] in vowels:
            current_vowel = vowels_present[-1]
            output = replace_string(output, i, current_vowel)
            vowels_present = vowels_present[:-1]
    return output
