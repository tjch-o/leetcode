def within_int(x):
    return -(2**31) <= x < 2**31 - 1


def reverse(x):
    negative = x < 0
    reversed = int(str(abs(x))[::-1])

    if not within_int(x) or not within_int(reversed):
        return 0

    if negative:
        reversed *= -1
    return reversed
