from collections import Counter


def find_lucky(arr):
    counts = Counter(arr)
    res = -1

    for key in counts:
        if key == counts[key]:
            res = max(res, key)
    return res
