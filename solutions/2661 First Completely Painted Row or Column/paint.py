from collections import defaultdict


def first_complete_index(arr, mat):
    m, n = len(mat), len(mat[0])
    num_to_pos_map = defaultdict(tuple)

    for i in range(m):
        for j in range(n):
            num_to_pos_map[mat[i][j]] = (i, j)

    rows_count = [0 for _ in range(m)]
    cols_count = [0 for _ in range(n)]

    for i, num in enumerate(arr):
        x, y = num_to_pos_map[num]
        rows_count[x] += 1
        cols_count[y] += 1

        if rows_count[x] == n or cols_count[y] == m:
            return i
