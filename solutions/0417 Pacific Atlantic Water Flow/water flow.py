def within_grid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def dfs(grid, i, j, visited, prev):
    # reversed direction so should check if the current cell is less than the previous
    if not within_grid(grid, i, j) or (i, j) in visited or grid[i][j] < prev:
        return

    curr = grid[i][j]
    visited.add((i, j))
    dfs(grid, i - 1, j, visited, curr)
    dfs(grid, i + 1, j, visited, curr)
    dfs(grid, i, j - 1, visited, curr)
    dfs(grid, i, j + 1, visited, curr)


def pacific_atlantic(heights):
    m, n = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()

    # reverse direction of flow of water (from ocean to cells) to avoid searching all cells
    for i in range(m):
        dfs(heights, i, 0, pacific, heights[i][0])
        dfs(heights, i, n - 1, atlantic, heights[i][n - 1])

    for j in range(n):
        dfs(heights, 0, j, pacific, heights[0][j])
        dfs(heights, m - 1, j, atlantic, heights[m - 1][j])

    result = []

    for i in range(m):
        for j in range(n):
            if (i, j) in pacific and (i, j) in atlantic:
                result.append((i, j))
    return result
