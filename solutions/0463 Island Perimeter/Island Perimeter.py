def dfs(grid, i, j, m, n, visited):
    # checking if current grid is water cannot be done before checking if it is the boundary
    if i < 0 or j < 0 or i > m - 1 or j > n - 1 or grid[i][j] == 0:
        return 1

    if visited[i][j]:
        return 0

    visited[i][j] = True
    perimeter = 0

    perimeter += dfs(grid, i, j - 1, m, n, visited)
    perimeter += dfs(grid, i, j + 1, m, n, visited)
    perimeter += dfs(grid, i - 1, j, m, n, visited)
    perimeter += dfs(grid, i + 1, j, m, n, visited)
    return perimeter


def island_perimeter(grid):
    m = len(grid)
    n = len(grid[0])
    perimeter = 0
    visited = [[False for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                perimeter += dfs(grid, i, j, m, n, visited)
    return perimeter
