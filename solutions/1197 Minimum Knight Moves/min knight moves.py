from collections import deque


def is_goal_state(i, j, x, y):
    return i == x and j == y


def min_knight_moves(x, y):
    directions = [
        (1, 2),
        (1, -2),
        (2, 1),
        (2, -1),
        (-1, 2),
        (-1, -2),
        (-2, 1),
        (-2, -1),
    ]
    queue = deque([(0, 0, 0)])
    visited = set()

    while queue:
        ci, cj, count = queue.popleft()

        if is_goal_state(ci, cj, x, y):
            return count

        if (ci, cj) in visited:
            continue

        visited.add((ci, cj))

        for d in directions:
            dx, dy = d
            ni, nj = ci + dx, cj + dy
            queue.append((ni, nj, count + 1))
    return -1
