def kth_factor(n, k):
    if k == 1:
        return 1
    elif n == 1 and k > 1:
        return -1

    factors = [1]

    for i in range(2, n + 1):
        if n % i == 0:
            factors.append(i)

    return -1 if len(factors) < k else factors[k - 1]
