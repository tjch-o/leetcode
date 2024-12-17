def w(x, y, z):
    return x * y * z


def min_score_triangulation(values):
    n = len(values)
    table = [[float("inf") for _ in range(n)] for _ in range(n)]

    for i in range(n):
        table[i][i] = 0

    for i in range(n - 1):
        table[i][i + 1] = 0

    for l in range(2, n):
        for i in range(n - l):
            j = i + l

            for k in range(i + 1, j):
                table[i][j] = min(
                    table[i][j],
                    table[i][k] + w(values[i], values[j], values[k]) + table[k][j],
                )
    return table[0][n - 1]
