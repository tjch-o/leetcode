def value_after_k_seconds(n, k):
    prev = [1] * n
    mod = 10**9 + 7

    for _ in range(k):
        curr = [0] * n
        for i in range(n):
            curr[i] = curr[i - 1] + prev[i]

        prev = curr
    return curr[-1] % mod
