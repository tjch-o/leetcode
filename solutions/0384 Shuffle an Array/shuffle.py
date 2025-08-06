import random


class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        arr = self.nums[:]
        n = len(arr)

        for i in range(n):
            j = random.randint(i, n - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
