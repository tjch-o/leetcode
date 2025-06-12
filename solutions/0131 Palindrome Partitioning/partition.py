def backtrack(s, start, curr, res, table):
    if start == len(s):
        res.append(curr[:])
        return

    for i in range(start, len(s)):
        if table[start][i]:
            curr.append(s[start : i + 1])
            backtrack(s, i + 1, curr, res, table)
            curr.pop()


def partition(s):
    n = len(s)
    table = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        table[i][i] = True

    for j in range(1, n):
        for i in range(j):
            if s[i] == s[j] and (j - i <= 1 or table[i + 1][j - 1]):
                table[i][j] = True

    res = []
    backtrack(s, 0, [], res, table)
    return res
