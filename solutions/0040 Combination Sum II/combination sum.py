def backtrack(candidates, target, ptr, curr, acc, res):
    if curr == target:
        res.append(acc)
        return

    for i in range(ptr, len(candidates)):
        if i > ptr and candidates[i] == candidates[i - 1]:
            continue

        if curr + candidates[i] > target:
            break

        backtrack(
            candidates, target, i + 1, curr + candidates[i], acc + [candidates[i]], res
        )


def combination_sum(candidates, target):
    res = []
    candidates.sort()
    backtrack(candidates, target, 0, 0, [], res)
    return res
