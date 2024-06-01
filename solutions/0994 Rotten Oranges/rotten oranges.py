from collections import deque

def within_grid(grid, i, j):
    return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

def get_rotten_oranges(grid):
    queue = deque()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
    return queue

def oranges_rotting(grid):
    m, n = len(grid), len(grid[0])
    queue = get_rotten_oranges(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    max_minutes = 0

    while queue:
        i, j, minutes = queue.popleft()
        # find the maximum number of minutes before there are no more rotten oranges
        max_minutes = max(max_minutes, minutes)
        
        for x, y in directions:
            ni, nj = i + x, j + y

            if within_grid(grid, ni, nj) and grid[ni][nj] == 1 and not visited[ni][nj]:
                queue.append((ni, nj, minutes + 1))
                visited[ni][nj] = True
                grid[ni][nj] = 2
    
    fresh_oranges_in_rows = [True if 1 in row else False for row in grid]

    if True in fresh_oranges_in_rows:
        return -1
    return max_minutes

assert oranges_rotting(grid = [[2,1,1],[1,1,0],[0,1,1]]) == 4
assert oranges_rotting(grid = [[2,1,1],[0,1,1],[1,0,1]]) == -1
assert oranges_rotting(grid = [[0,2]]) == 0
assert oranges_rotting(grid = [[0]]) == 0
assert oranges_rotting(grid = [[1, 2]]) == 1
assert oranges_rotting(grid = [[2,1,1],[1,1,1],[0,1,2]]) == 2
