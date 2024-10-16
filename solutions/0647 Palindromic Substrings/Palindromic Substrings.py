def count_substrings(s):
    count = 0
    n = len(s)
    table = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        table[i][i] = True
        count += 1

    for j in range(1, n):
        for i in range(j):
            if s[i] == s[j] and (j - i <= 1 or table[i + 1][j - 1]):
                table[i][j] = True
                count += 1
    return count
