from collections import defaultdict


def group_anagrams(strs):
    counts = defaultdict(list)

    for s in strs:
        sorted_s = "".join(sorted(list(s)))
        counts[sorted_s].append(s)

    result = []
    for val in counts.values():
        result.append(val)
    return result
