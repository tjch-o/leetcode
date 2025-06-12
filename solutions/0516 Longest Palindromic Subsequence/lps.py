def longest_palindromic_subsequence(s):
    n = len(s)
    table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        table[i][i] = 1

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1

            if s[start] == s[end]:
                table[start][end] = table[start + 1][end - 1] + 2
            else:
                table[start][end] = max(table[start + 1][end], table[start][end - 1])
    return table[0][n - 1]
