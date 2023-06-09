def rob(nums):
   # cannot rob consecutive houses
   if len(nums) == 1: 
      return nums[0]

   table = [0 for _ in range(len(nums))]
   table[0] = nums[0]  
   table[1] = max(nums[0], nums[1])

   for i in range(2,len(nums)): \
      table[i] = max(table[i - 1], table[i - 2] + nums[i])
   return table[len(nums) - 1]  