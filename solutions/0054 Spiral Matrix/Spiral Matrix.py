def spiral_order(matrix):
    m, n = len(matrix), len(matrix[0])
    up, down = 0, m - 1
    left, right = 0, n - 1
    result = []
    visited = set()

    while left <= right and up <= down:
        for j in range(left, right + 1):
            if (up, j) not in visited:
                result.append(matrix[up][j])
                visited.add((up, j))

        up += 1

        for i in range(up, down + 1):
            if (i, right) not in visited:
                result.append(matrix[i][right])
                visited.add((i, right))

        right -= 1

        for j in range(right, left - 1, -1):
            if (down, j) not in visited:
                result.append(matrix[down][j])
                visited.add((down, j))

        down -= 1

        for i in range(down, up - 1, -1):
            if (i, left) not in visited:
                result.append(matrix[i][left])
                visited.add((i, left))

        left += 1

    return result
