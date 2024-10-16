from collections import deque


def within_grid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def walls_and_gates(rooms):
    def within_grid(grid, i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])

    m, n = len(rooms), len(rooms[0])
    gates = []

    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                gates.append((i, j, 0))

    visited = set()
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    q = deque(gates)

    while q:
        ci, cj, d = q.popleft()

        if (ci, cj) in visited or rooms[ci][cj] == -1:
            continue

        visited.add((ci, cj))
        rooms[ci][cj] = d

        for x, y in directions:
            ni, nj = ci + x, cj + y

            if within_grid(rooms, ni, nj):
                q.append((ni, nj, d + 1))
