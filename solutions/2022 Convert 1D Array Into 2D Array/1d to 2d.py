def construct_2d_array(original, m, n):
    original_len = len(original)

    if m * n != original_len:
        return []

    res = []
    for i in range(m):
        res.append([])
        for j in range(n):
            if i * n + j < original_len:
                res[i].append(original[i * n + j])
    return res
