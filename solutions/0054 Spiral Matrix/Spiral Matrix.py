def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    output = []

    row_low = 0
    row_high = m - 1
    col_low = 0
    col_high = n - 1

    while row_low <= row_high and col_low <= col_high:
        for i in range(col_low, col_high + 1):
            output.append(matrix[row_low][i])
        row_low += 1

        for i in range(row_low, row_high + 1):
            output.append(matrix[i][col_high])
        col_high -= 1

        # the if case for both is to prevent double counting when there is only one row and column left
        if row_low <= row_high and col_low <= col_high:
            for i in range(col_high, col_low - 1, -1):
                output.append(matrix[row_high][i])
            row_high -= 1

        if row_low <= row_high and col_low <= col_high:
            for i in range(row_high, row_low - 1, -1):
                output.append(matrix[i][col_low])
            col_low += 1

    return output
