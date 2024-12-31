from collections import defaultdict


def character_replacement(s, k):
    counts = defaultdict(int)
    max_count = 0
    max_l = 0
    start = 0

    for i, c in enumerate(s):
        counts[c] += 1
        max_count = max(max_count, counts[c])

        if i - start + 1 - max_count > k:
            counts[s[start]] -= 1
            start += 1

        max_l = max(max_l, i - start + 1)
    return max_l
