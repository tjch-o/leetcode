def subsets(nums):
   # note that number of elements is basically 2**nums
   if len(nums) == 1:
      return [[], nums]
   
   result = [[]]
   for element in nums:
      combinations = [i + [element] for i in result]
      # extend instead of append because extend adds one whole list of combinations without it being nested
      result.extend(combinations) 
   return result