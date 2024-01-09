def productExceptSelf(nums):
    n = len(nums)
    answer = []
    product_left_elements = [1 for _ in range(n)]
    product_right_elements = [1 for _ in range(n)]

    for i in range(1, n):
        product_left_elements[i] = product_left_elements[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        product_right_elements[i] = product_right_elements[i + 1] * nums[i + 1]

    for i in range(n):
        answer.append(product_left_elements[i] * product_right_elements[i])
    return answer
