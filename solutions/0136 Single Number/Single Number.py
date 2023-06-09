def singleNumber(nums):
     # linear time complexity and constant extra space so a loop
     for element in set(nums):
         count = nums.count(element)
         if count == 1:
            return element
