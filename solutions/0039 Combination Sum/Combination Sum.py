def dfs(start, curr_combi, result, candidates, target):
    if target == 0:
        x = [val for val in curr_combi]
        result.append(x)
        return

    for i in range(start, len(candidates)):
        curr_val = candidates[i]

        if curr_val <= target:
            curr_combi.append(curr_val)
            # passing in i allows the same value to be picked unlimited times
            dfs(i, curr_combi, result, candidates, target - curr_val)
            # backtrack if cannot find value
            curr_combi.pop()


def combination_sum(candidates, target):
    result = []
    dfs(0, [], result, candidates, target)
    return result
