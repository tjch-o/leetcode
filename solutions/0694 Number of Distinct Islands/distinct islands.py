def within_grid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def backtrack(grid, i, j, move, path, visited):
    if not within_grid(grid, i, j) or grid[i][j] == 0 or visited[i][j]:
        return

    visited[i][j] = True
    path.append(move)
    backtrack(grid, i - 1, j, "U", path, visited)
    backtrack(grid, i + 1, j, "D", path, visited)
    backtrack(grid, i, j - 1, "L", path, visited)
    backtrack(grid, i, j + 1, "R", path, visited)
    path.append("O")


def num_distinct_islands(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    distinct_islands = set()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                path = []
                backtrack(grid, i, j, "X", path, visited)
                distinct_islands.add("".join(path))
    return len(distinct_islands)
