def inplace_reverse(arr):
    n = len(arr)
    num_iterations = n // 2

    for i in range(0, num_iterations):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr


def next_permutation(nums):
    n = len(nums)
    rightmost_incr = -1

    for i in range(n - 1, 0, -1):
        first, second = nums[i - 1], nums[i]
        if first < second:
            rightmost_incr = i - 1
            break

    if rightmost_incr != -1:
        pivot = nums[rightmost_incr]
        smallest_greater_pivot = float("inf")
        smallest_greater_pivot_index = -1

        for i in range(n - 1, rightmost_incr, -1):
            if pivot < nums[i] < smallest_greater_pivot:
                smallest_greater_pivot = nums[i]
                smallest_greater_pivot_index = i

        nums[rightmost_incr], nums[smallest_greater_pivot_index] = (
            nums[smallest_greater_pivot_index],
            nums[rightmost_incr],
        )

    nums[rightmost_incr + 1 :] = inplace_reverse(nums[rightmost_incr + 1 :])
