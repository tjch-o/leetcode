def within_grid(matrix, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


def dfs(matrix, i, j, table):
    if table[i][j] != -1:
        return table[i][j]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_len = 1

    for x, y in directions:
        ni, nj = i + x, j + y

        if within_grid(matrix, ni, nj) and matrix[ni][nj] > matrix[i][j]:
            max_len = max(max_len, dfs(matrix, ni, nj, table) + 1)

    table[i][j] = max_len
    return max_len


def longest_increasing_path(matrix):
    m, n = len(matrix), len(matrix[0])
    table = [[-1 for _ in range(n)] for _ in range(m)]
    max_path = 0

    for i in range(m):
        for j in range(n):
            max_path = max(max_path, dfs(matrix, i, j, table))
    return max_path
