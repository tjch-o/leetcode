from math import ceil


def repeated_string_match(a, b):
    min_repeats = ceil(len(b) / len(a))

    if b in min_repeats * a:
        return min_repeats
    if b in (min_repeats + 1) * a:
        return min_repeats + 1
    return -1
