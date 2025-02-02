def count_servers(grid):
    m, n = len(grid), len(grid[0])
    count = 0
    row_count = [0 for _ in range(m)]
    col_count = [0 for _ in range(n)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                row_count[i] += 1
                col_count[j] += 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                if row_count[i] > 1 or col_count[j] > 1:
                    count += 1
    return count
