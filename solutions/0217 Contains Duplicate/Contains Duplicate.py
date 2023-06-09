def containsDuplicate(nums):
   nums.sort()
   for i in range(1,len(nums)):
      if nums[i-1] == nums[i]:
         return True
   return False
