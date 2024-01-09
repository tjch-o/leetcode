def reverse(x):
    s = str(x)
    reversed_s = s[::-1]

    if s[0] == "-":
        reversed_s = reversed_s[-1] + reversed_s[:-1]

    reversed_s = int(reversed_s)
    if reversed_s < -(2**31) or reversed_s >= 2**31:
        return 0
    return reversed_s
