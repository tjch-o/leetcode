def within_grid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def dfs(grid, i, j):
    if not within_grid(grid, i, j) or grid[i][j] == "0":
        return

    grid[i][j] = "0"
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)


def num_islands(grid):
    m, n = len(grid), len(grid[0])
    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count += 1
                dfs(grid, i, j)
    return count
