from collections import Counter


def find_difference(s, t):
    count = Counter(s)
    new_count = Counter(t)

    for key in new_count:
        if key not in count:
            return key
        elif count[key] != new_count[key]:
            return key
