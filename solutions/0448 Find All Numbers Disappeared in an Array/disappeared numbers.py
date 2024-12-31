def find_disappeared_numbers(nums):
    n = len(nums)
    seen = [0 for _ in range(n + 1)]

    for num in nums:
        seen[num] = 1

    missing = []
    for i in range(1, n + 1):
        if seen[i] == 0:
            missing.append(i)
    return missing
