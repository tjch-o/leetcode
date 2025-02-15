def longest_common_subsequence(s1, s2):
    if not s1 or not s2:
        return 0

    m, n = len(s1), len(s2)
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = max(table[i][j], table[i - 1][j - 1] + 1)
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[m][n]
