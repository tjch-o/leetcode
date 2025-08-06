def spiral_order(matrix):
    m, n = len(matrix), len(matrix[0])
    left, right, up, down = 0, n - 1, 0, m - 1
    res = []

    while left <= right and up <= down:
        for i in range(left, right + 1):
            res.append(matrix[up][i])
        up += 1

        for j in range(up, down + 1):
            res.append(matrix[j][right])
        right -= 1

        if up <= down:
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1

        if left <= right:
            for j in range(down, up - 1, -1):
                res.append(matrix[j][left])
            left += 1
    return res
