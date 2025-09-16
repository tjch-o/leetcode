def rotate_the_box(box_grid):
    m, n = len(box_grid), len(box_grid[0])
    rotated = [[None for _ in range(m)] for _ in range(n)]

    for i in range(m):
        for j in range(n):
            rotated[j][m - i - 1] = box_grid[i][j]

    for col in range(m):
        bottom = n - 1
        for row in range(n - 1, -1, -1):
            if rotated[row][col] == "*":
                bottom = row - 1
            elif rotated[row][col] == "#":
                rotated[row][col], rotated[bottom][col] = (
                    rotated[bottom][col],
                    rotated[row][col],
                )
                bottom -= 1
    return rotated
