import heapq


def within_grid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def minimum_effort_path(heights):
    m, n = len(heights), len(heights[0])
    heap = [(0, 0, 0)]
    heapq.heapify(heap)
    visited = set()

    while heap:
        effort, i, j = heapq.heappop(heap)

        if i == m - 1 and j == n - 1:
            return effort

        if (i, j) in visited:
            continue

        visited.add((i, j))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for x, y in dirs:
            ni, nj = i + x, j + y

            if within_grid(heights, ni, nj) and (ni, nj) not in visited:
                d = abs(heights[i][j] - heights[ni][nj])
                new_effort = max(effort, d)
                heapq.heappush(heap, (new_effort, ni, nj))
