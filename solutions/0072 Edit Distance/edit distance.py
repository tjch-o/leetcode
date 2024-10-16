def min_distance(word_1, word_2):
    if word_1 == word_2:
        return 0

    m, n = len(word_1), len(word_2)
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        table[i][0] = i

    for j in range(n + 1):
        table[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word_1[i - 1] == word_2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = min(
                    table[i - 1][j] + 1, table[i][j - 1] + 1, table[i - 1][j - 1] + 1
                )
    return table[m][n]
