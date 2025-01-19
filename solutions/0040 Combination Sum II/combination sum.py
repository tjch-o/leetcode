def combination_sum_helper(candidates, target, idx, curr, path, res):
    if curr == target:
        res.append(path[:])
        return

    for i in range(idx, len(candidates)):
        if i > idx and candidates[i] == candidates[i - 1]:
            continue

        if curr + candidates[i] > target:
            break

        path.append(candidates[i])
        combination_sum_helper(
            candidates, target, i + 1, curr + candidates[i], path, res
        )
        path.pop()


def combination_sum(candidates, target):
    res = []
    candidates.sort()
    combination_sum_helper(candidates, target, 0, 0, [], res)
    return res
