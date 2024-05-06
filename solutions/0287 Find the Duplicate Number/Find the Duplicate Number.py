def find_duplicate(nums):
    slow_ptr = 0
    fast_ptr = 0
    
    while True:
        slow_ptr = nums[slow_ptr]
        fast_ptr = nums[nums[fast_ptr]]
        
        if slow_ptr == fast_ptr:
            break
        
    other_slow_ptr = 0
    
    while True:
        slow_ptr = nums[slow_ptr]
        other_slow_ptr = nums[other_slow_ptr]
        
        if slow_ptr == other_slow_ptr:
            break
        
    return slow_ptr
