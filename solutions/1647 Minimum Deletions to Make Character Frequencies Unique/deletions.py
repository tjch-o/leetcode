from collections import Counter


def min_deletions(s):
    frequencies = Counter(s)
    deletions = 0
    seen = set()

    pairs = list(frequencies.items())
    pairs.sort(key=lambda x: x[1], reverse=True)

    for val, freq in pairs:
        while freq > 0 and freq in seen:
            freq -= 1
            deletions += 1

        if freq > 0:
            seen.add(freq)
    return deletions
