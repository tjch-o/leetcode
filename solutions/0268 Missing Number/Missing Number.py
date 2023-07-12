def missingNumber(nums):
   nums.sort()
   
   for i, j in enumerate(nums):
      if i != j:
         return i
      
   return len(nums)   