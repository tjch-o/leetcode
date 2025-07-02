import math


def get_divisor_sum(arr, d):
    res = 0

    for num in arr:
        res += math.ceil(num / d)
    return res


def find_smallest_divisor(nums, threshold):
    left, right = 1, max(nums)

    while left < right:
        mid = (left + right) // 2

        if get_divisor_sum(nums, mid) <= threshold:
            right = mid
        else:
            left = mid + 1
    return left
