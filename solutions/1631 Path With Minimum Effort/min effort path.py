import heapq


def within_grid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def min_effort_path(heights):
    m, n = len(heights), len(heights[0])
    table = [[float("inf") for _ in range(n)] for _ in range(m)]
    table[0][0] = 0

    heap = [(0, 0, 0)]
    heapq.heapify(heap)

    while heap:
        curr, i, j = heapq.heappop(heap)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        if i == m - 1 and j == n - 1:
            return curr

        for x, y in directions:
            ni, nj = x + i, y + j

            if within_grid(heights, ni, nj):
                next_effort = max(curr, abs(heights[ni][nj] - heights[i][j]))

                if next_effort < table[ni][nj]:
                    table[ni][nj] = next_effort
                    heapq.heappush(heap, (next_effort, ni, nj))
    return -1
