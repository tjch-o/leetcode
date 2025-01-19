def is_distinct(s):
    return len(s) == len(set(s))


def min_operations(nums):
    count = 0

    while nums and not is_distinct(nums):
        for _ in range(3):
            if nums:
                nums.pop(0)

        count += 1
    return count
