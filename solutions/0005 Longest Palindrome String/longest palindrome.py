def longest_palindrome(s):
    if not s:
        return s

    n = len(s)
    table = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        table[i][i] = True

    max_length = 1
    res = s[0]

    for j in range(1, n):
        for i in range(j):
            if s[i] == s[j]:
                if j - i <= 1 or table[i + 1][j - 1]:
                    table[i][j] = True
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        res = s[i : j + 1]
    return res
