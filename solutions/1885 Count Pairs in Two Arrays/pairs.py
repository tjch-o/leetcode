def count_pairs(nums1, nums2):
    n = len(nums1)
    diff = [nums1[i] - nums2[i] for i in range(n)]
    diff.sort()

    left, right = 0, n - 1
    count = 0

    while left <= right:
        if diff[left] + diff[right] > 0:
            count += right - left
            right -= 1
        else:
            left += 1
    return count
