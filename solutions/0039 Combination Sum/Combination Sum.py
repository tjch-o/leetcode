def combination_sum(candidates, target):
    table = [[] for _ in range(target + 1)]
    table[0] = [[]]

    for i in range(1, target + 1):
        for num in candidates:
            if i - num >= 0:
                for elem in table[i - num]:
                    # avoid duplicates by ensuring combination is sorted
                    if not elem or num >= elem[-1]:
                        table[i].append(elem + [num])

    return table[target]
