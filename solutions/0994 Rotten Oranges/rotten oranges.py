from collections import deque


def within_grid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def oranges_rotting(grid):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    max_minutes_before_rotten = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                queue.append((i, j, 0))

    while queue:
        i, j, minutes = queue.popleft()
        max_minutes_before_rotten = max(max_minutes_before_rotten, minutes)

        for x, y in directions:
            ni, nj = i + x, j + y

            if within_grid(grid, ni, nj) and grid[ni][nj] == 1 and not visited[ni][nj]:
                grid[ni][nj] = 2
                visited[ni][nj] = True
                queue.append((ni, nj, minutes + 1))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return -1
    return max_minutes_before_rotten
