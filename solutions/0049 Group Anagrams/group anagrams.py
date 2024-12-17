from collections import defaultdict


def group_anagrams(strs):
    anagrams = defaultdict(list)

    for s in strs:
        chars = sorted(list(s))
        sorted_word = "".join(chars)
        anagrams[sorted_word].append(s)
    return list(anagrams.values())
