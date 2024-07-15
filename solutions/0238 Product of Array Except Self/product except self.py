def product_except_self(nums):
    n = len(nums)
    left_prod = [0] * n
    right_prod = [0] * n

    left_prod[0] = 1
    right_prod[-1] = 1
    result = []

    for i in range(1, n):
        left_prod[i] = left_prod[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right_prod[i] = right_prod[i + 1] * nums[i + 1]

    for i in range(n):
        result.append(left_prod[i] * right_prod[i])
    return result
