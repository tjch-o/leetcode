from collections import deque


def within_grid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def oranges_rotting(grid):
    m, n = len(grid), len(grid[0])
    time = [[float("inf") for _ in range(n)] for _ in range(m)]
    queue = deque()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                time[i][j] = 0
                queue.append((i, j))
            elif grid[i][j] == 0:
                time[i][j] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        i, j = queue.popleft()

        for x, y in directions:
            ni, nj = i + x, j + y

            if within_grid(grid, ni, nj):
                if grid[ni][nj] == 1 and time[ni][nj] > time[i][j] + 1:
                    time[ni][nj] = time[i][j] + 1
                    queue.append((ni, nj))

    max_time = 0
    for i in range(m):
        for j in range(n):
            if time[i][j] == float("inf"):
                return -1

            max_time = max(max_time, time[i][j])
    return max_time
