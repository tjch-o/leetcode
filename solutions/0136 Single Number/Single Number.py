def singleNumber(nums):
     for element in set(nums):
         count = nums.count(element)
         if count == 1:
            return element
