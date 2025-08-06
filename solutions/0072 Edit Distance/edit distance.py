def min_distance(w1, w2):
    if w1 == w2:
        return 0

    m, n = len(w1), len(w2)
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        table[i][0] = i

    for j in range(n + 1):
        table[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if w1[i - 1] == w2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = min(
                    table[i - 1][j] + 1, table[i][j - 1] + 1, table[i - 1][j - 1] + 1
                )
    return table[m][n]
