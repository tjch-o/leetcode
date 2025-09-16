from collections import defaultdict


def start_end_both_vowels(s):
    vowels = {"a", "e", "i", "o", "u"}
    return s[0] in vowels and s[-1] in vowels


def vowel_strings(words, queries):
    prefix_map = defaultdict(int)
    n = len(words)

    for i in range(n):
        if i == 0 and start_end_both_vowels(words[i]):
            prefix_map[i] += 1
        elif start_end_both_vowels(words[i]):
            prefix_map[i] = prefix_map[i - 1] + 1
        else:
            prefix_map[i] = prefix_map[i - 1]

    res = []
    for start, end in queries:
        if start == 0:
            res.append(prefix_map[end])
        else:
            res.append(prefix_map[end] - prefix_map[start - 1])
    return res
