from collections import Counter


def min_rounds_per_difficulty(x):
    if x == 1:
        return -1
    if x == 2 or x == 3:
        return 1
    return (x + 2) // 3


def minimum_rounds(tasks):
    counts = Counter(tasks)
    res = 0

    for level in counts:
        rounds = min_rounds_per_difficulty(counts[level])
        if rounds == -1:
            return -1
        res += rounds
    return res
