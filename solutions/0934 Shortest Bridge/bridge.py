from collections import deque


def within_grid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def dfs(grid, i, j, island):
    if not within_grid(grid, i, j) or grid[i][j] != 1:
        return

    grid[i][j] = 2
    island.append((i, j))
    dfs(grid, i - 1, j, island)
    dfs(grid, i + 1, j, island)
    dfs(grid, i, j - 1, island)
    dfs(grid, i, j + 1, island)


def shortest_bridge(grid):
    m, n = len(grid), len(grid[0])
    found = False
    island = []

    for i in range(m):
        if found:
            break

        for j in range(n):
            if grid[i][j] == 1:
                dfs(grid, i, j, island)
                found = True
                break

    queue = deque()
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i, j in island:
        queue.append((i, j, 0))
        visited.add((i, j))

    while queue:
        i, j, dist = queue.popleft()

        for x, y in directions:
            ni, nj = i + x, j + y

            if within_grid(grid, ni, nj) and (ni, nj) not in visited:
                if grid[ni][nj] == 1:
                    return dist

                queue.append((ni, nj, dist + 1))
                visited.add((ni, nj))
    return -1
