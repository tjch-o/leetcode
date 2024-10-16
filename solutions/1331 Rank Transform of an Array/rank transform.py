def array_rank_transform(arr):
    nums = []
    res = []

    for i, num in enumerate(arr):
        nums.append((num, i))

    nums.sort(key=lambda x: x[0])
    ranks = {}
    rank = 0

    for num, _ in nums:
        if num not in ranks:
            rank += 1
            ranks[num] = rank

    for i in range(len(arr)):
        res.append(ranks[arr[i]])
    return res
