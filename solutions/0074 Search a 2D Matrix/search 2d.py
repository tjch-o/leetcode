def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    row_ptr = 0
    col_ptr = n - 1

    while 0 <= row_ptr < m and 0 <= col_ptr < n:
        curr = matrix[row_ptr][col_ptr]

        if curr == target:
            return True
        elif curr < target:
            row_ptr += 1
        else:
            col_ptr -= 1
    return False
