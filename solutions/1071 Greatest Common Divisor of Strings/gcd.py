def gcd(a, b):
    if b > a:
        a, b = b, a

    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_strings(s1, s2):
    if s1 + s2 != s2 + s1:
        return ""

    l = gcd(len(s1), len(s2))
    return s1[:l]
