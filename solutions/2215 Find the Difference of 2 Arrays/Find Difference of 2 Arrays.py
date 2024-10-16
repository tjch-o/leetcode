def find_difference(nums1, nums2):
    s1 = set(nums1)
    s2 = set(nums2)
    d1 = s1.difference(s2)
    d2 = s2.difference(s1)
    return [d1, d2]
