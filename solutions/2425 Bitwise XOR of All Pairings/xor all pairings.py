def xor_all_nums(nums1, nums2):
    m, n = len(nums1), len(nums2)
    xor1 = 0
    xor2 = 0

    for i in range(m):
        xor1 ^= nums1[i]

    for j in range(n):
        xor2 ^= nums2[j]

    res = 0
    if n % 2 != 0:
        res ^= xor1
    if m % 2 != 0:
        res ^= xor2
    return res
