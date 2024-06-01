from collections import deque
from copy import copy


def within_grid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def update_matrix(mat):
    m, n = len(mat), len(mat[0])
    queue = deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = copy(mat)

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                result[i][j] = 0
                queue.append((i, j, 0))
            else:
                result[i][j] = float("inf")

    while queue:
        i, j, count = queue.popleft()

        for x, y in directions:
            ni, nj = i + x, j + y

            if within_grid(mat, ni, nj):
                if result[ni][nj] > count + 1:
                    result[ni][nj] = count + 1
                    queue.append((ni, nj, count + 1))

    return result
