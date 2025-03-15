import heapq


def within_grid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    table = [[float("inf") for _ in range(n)] for _ in range(m)]
    heap = [(grid[0][0], 0, 0)]
    heapq.heapify(heap)

    while heap:
        curr, i, j = heapq.heappop(heap)

        if i == m - 1 and j == n - 1:
            return curr

        directions = [(1, 0), (0, 1)]

        for x, y in directions:
            ni, nj = i + x, j + y

            if within_grid(grid, ni, nj):
                move_sum = curr + grid[ni][nj]

                if move_sum < table[ni][nj]:
                    table[ni][nj] = move_sum
                    heapq.heappush(heap, (move_sum, ni, nj))
    return -1
