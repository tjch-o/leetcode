def num_distinct(s, t):
    m, n = len(s), len(t)
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m):
        table[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                table[i][j] = table[i - 1][j - 1] + table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j]
    return table[m][n]
