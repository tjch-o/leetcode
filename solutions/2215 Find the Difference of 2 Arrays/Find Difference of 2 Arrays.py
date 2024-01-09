def findDifference(nums1, nums2):
    set_1 = set(nums1)
    set_2 = set(nums2)
    distinct_set_1 = set_1.difference(set_2)
    distinct_set_2 = set_2.difference(set_1)
    return [distinct_set_1, distinct_set_2]
