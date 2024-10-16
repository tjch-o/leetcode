def len_longest_fib_subseq(arr):
    n = len(arr)
    index_map = {}

    for i, val in enumerate(arr):
        index_map[val] = i

    table = {}
    l = 0

    for j in range(n):
        for i in range(j):
            d = arr[j] - arr[i]

            if d < arr[i] and d in index_map:
                k = index_map[d]
                table[(i, j)] = table.get((k, i), 2) + 1
                l = max(l, table[(i, j)])

    if l >= 3:
        return l
    return 0
