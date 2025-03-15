def unique_paths_with_obstacles(grid):
    if grid[0][0] == 1:
        return 0

    m, n = len(grid), len(grid[0])
    table = [[0 for _ in range(n)] for _ in range(m)]
    table[0][0] = 1

    for i in range(1, m):
        if grid[i][0] == 1:
            break

        table[i][0] = 1

    for j in range(1, n):
        if grid[0][j] == 1:
            break

        table[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] != 1:
                table[i][j] = table[i - 1][j] + table[i][j - 1]
    return table[m - 1][n - 1]
