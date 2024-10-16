def lcs(s1, s2):
    m, n = len(s1), len(s2)
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = max(table[i][j], table[i - 1][j - 1] + 1)
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    res = []
    i = m
    j = n

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            res.append(s1[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(res[::-1])


def shortest_common_supersequence(s1, s2):
    if s1 == s2:
        return s1

    lcs_seq = lcs(s1, s2)
    m, n = len(s1), len(s2)
    i = 0
    j = 0
    res = []

    for c in lcs_seq:
        while i < m and s1[i] != c:
            res.append(s1[i])
            i += 1

        while j < n and s2[j] != c:
            res.append(s2[j])
            j += 1

        res.append(s1[i])
        i += 1
        j += 1

    res.extend(s1[i:])
    res.extend(s2[j:])
    return "".join(res)
