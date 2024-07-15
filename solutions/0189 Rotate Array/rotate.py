def rotate(nums, k):
    def reverse_inplace(lst, start, end):
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
    
    if k == 0:
        return nums
    elif k > len(nums):
        k = k % len(nums)
    
    reverse_inplace(nums, 0, len(nums) - 1) 
    reverse_inplace(nums, 0, k - 1) 
    reverse_inplace(nums, k, len(nums) - 1)
    return nums