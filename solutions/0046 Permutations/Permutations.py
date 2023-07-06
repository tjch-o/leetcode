def permute(nums):
   if len(nums) == 0:
      return []
   elif len(nums) == 1:
      return [nums]
   else:
      result = []
      
      for i in range(len(nums)):
         current_element = nums[i]
         remaining_lst = nums[:i] + nums[i + 1:]
         for p in permute(remaining_lst): 
            result.append([current_element] + p)
                  
      return result