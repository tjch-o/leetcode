def last_stone_weight(stones):
    total = sum(stones)
    target = total // 2
    table = [False for _ in range(target + 1)]
    table[0] = True

    for stone in stones:
        for i in range(target, stone - 1, -1):
            table[i] = table[i] or table[i - stone]

    max_weight = 0
    for i in range(target, -1, -1):
        if table[i]:
            max_weight = i
            break
    return total - max_weight * 2
