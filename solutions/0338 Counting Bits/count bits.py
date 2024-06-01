def count_bits(n):
    result = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        lsb = i & 1
        result[i] = result[i >> 1] + lsb
    return result
