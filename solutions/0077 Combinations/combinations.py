def backtrack(n, k, start, x, curr, res):
    if x == k:
        res.append(curr[:])
        return

    for i in range(start, n + 1):
        curr.append(i)
        backtrack(n, k, i + 1, x + 1, curr, res)
        curr.pop()


def combine(n, k):
    res = []
    backtrack(n, k, 1, 0, [], res)
    return res
