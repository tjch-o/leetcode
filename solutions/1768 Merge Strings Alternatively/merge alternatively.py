def merge_alternatively(w1, w2):
    if not w1 and not w2:
        return ""

    n1, n2 = len(w1), len(w2)
    longer_s = w1 if n1 > n2 else w2
    res = ""

    for i in range(min(n1, n2)):
        res += w1[i]
        res += w2[i]

    for j in range(max(n1, n2) - min(n1, n2)):
        res += longer_s[min(n1, n2) + j]
    return res
