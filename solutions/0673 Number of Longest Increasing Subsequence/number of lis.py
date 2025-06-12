def find_number_of_lis(nums):
    n = len(nums)
    lengths = [1 for _ in range(n)]
    counts = [1 for _ in range(n)]

    for j in range(1, n):
        for i in range(j):
            if nums[j] > nums[i]:
                if lengths[i] + 1 > lengths[j]:
                    lengths[j] = lengths[i] + 1
                    counts[j] = counts[i]
                elif lengths[i] + 1 == lengths[j]:
                    counts[j] += counts[i]

    max_l = max(lengths)
    total = 0

    for i in range(n):
        if lengths[i] == max_l:
            total += counts[i]
    return total
