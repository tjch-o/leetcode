from collections import defaultdict


def character_replacement(s, k):
    n = len(s)
    freq = defaultdict(int)
    left = 0
    max_count, max_length = 0, 0

    for i in range(n):
        freq[s[i]] += 1
        max_count = max(max_count, freq[s[i]])

        if (i - left + 1 - max_count) > k:
            freq[s[left]] -= 1
            left += 1

        max_length = max(max_length, i - left + 1)
    return max_length
