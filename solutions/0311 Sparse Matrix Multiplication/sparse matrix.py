from collections import defaultdict


def multiply(A, B):
    m, n = len(A), len(A[0])
    n2, p = len(B), len(B[0])

    b_dict = defaultdict(list)

    for j in range(n2):
        for k in range(p):
            if B[j][k] != 0:
                b_dict[j].append((k, B[j][k]))

    res = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if A[i][j] != 0:
                for k, val in b_dict[j]:
                    res[i][k] += A[i][j] * val
    return res
