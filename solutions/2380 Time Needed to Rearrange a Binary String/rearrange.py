def seconds_to_remove_occurrences(s):
    zeroes = 0
    res = 0

    for c in s:
        if c == "0":
            zeroes += 1
        else:
            if zeroes > 0:
                res = max(res + 1, zeroes)
    return res
