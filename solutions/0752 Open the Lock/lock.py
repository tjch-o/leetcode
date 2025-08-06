from collections import deque


def open_lock(deadends, target):
    starting = "0000"
    visited = set()
    deadends = set(deadends)

    if starting in deadends:
        return -1

    queue = deque()
    queue.append((starting, 0))

    while queue:
        curr, turn = queue.popleft()

        if curr == target:
            return turn

        if curr in visited:
            continue

        visited.add(curr)

        for i in range(len(target)):
            directions = [1, -1]

            for x in directions:
                new_c = (int(curr[i]) + x) % 10
                next_combination = curr[:i] + str(new_c) + curr[i + 1 :]

                if next_combination not in deadends:
                    queue.append((next_combination, turn + 1))
    return -1
