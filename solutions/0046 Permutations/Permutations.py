def backtrack(nums, d, curr, res, visited):
    if d == len(nums):
        res.append([x for x in curr])
        return res

    for i, num in enumerate(nums):
        if visited[i]:
            continue

        curr.append(num)
        visited[i] = True
        backtrack(nums, d + 1, curr, res, visited)
        curr.pop()
        visited[i] = False


def permute(nums):
    res = []
    visited = [False for _ in range(len(nums))]
    backtrack(nums, 0, [], res, visited)
    return res
