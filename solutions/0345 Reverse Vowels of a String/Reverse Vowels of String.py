def replace_string(s, i, char):
    return s[:i] + char + s[i + 1 :]

def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    n = len(s)
    vowels_in_str = []
    output = s

    if n == 1:
        return s

    for char in s:
        if char in vowels:
            vowels_in_str.append(char)

    for i in range(n):
        if s[i] in vowels:
            current_vowel = vowels_in_str[-1]
            output = replace_string(output, i, current_vowel)
            vowels_in_str = vowels_in_str[:-1]

    return output
