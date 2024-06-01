def number_of_pairs(nums1, nums2, k):
    count = 0

    for x in nums1:
        for y in nums2:
            if x % (y * k) == 0:
                count += 1
    return count
