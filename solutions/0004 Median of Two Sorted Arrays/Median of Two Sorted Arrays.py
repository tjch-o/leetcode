import math

def findMedianSortedArrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    total = m + n
    is_odd = False
    
    if total % 2 != 0:
        median = math.floor(total / 2)
        is_odd = True
    else:
        median = math.floor((total - 1) / 2)
        is_odd = False
    
    output = []
    while (nums1 and nums2):
        head1 = nums1[0]
        head2 = nums2[0]
        if head1 <= head2:
            output.append(head1)
            nums1.pop(0)
        else:
            output.append(head2)
            nums2.pop(0)
            
    output.extend(nums1)
    output.extend(nums2)
    
    if is_odd:
        return output[median]
    else:
        return (output[median] + output[median + 1]) / 2 