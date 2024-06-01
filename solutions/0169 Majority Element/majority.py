def majority_element(nums):
    m = float("inf")
    count = 0

    for num in nums:
        if count == 0:
            m = num
            count += 1
        elif m == num:
            count += 1
        elif m != num:
            count -= 1
    return m
