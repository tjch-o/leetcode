def within_grid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def dfs(grid, i, j, visited):
    if not within_grid(grid, i, j) or (i, j) in visited or grid[i][j] == 0:
        return 0

    visited.add((i, j))
    return 1 + (
        dfs(grid, i - 1, j, visited)
        + dfs(grid, i + 1, j, visited)
        + dfs(grid, i, j - 1, visited)
        + dfs(grid, i, j + 1, visited)
    )


def max_area_of_island(grid):
    m, n = len(grid), len(grid[0])
    visited = set()

    max_area = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                curr = dfs(grid, i, j, visited)
                max_area = max(max_area, curr)
    return max_area
