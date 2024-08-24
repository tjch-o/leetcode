import random

class Solution:
    def __init__(self, w):
        self.weights = w
        self.sum = sum(w)
        self.prefix_sums = []
        curr = 0

        for weight in w:
            curr += weight
            self.prefix_sums.append(curr)
        
        
    def pick_index(self):
        x = random.randint(0, self.sum - 1)
        left, right = 0, len(self.weights) - 1

        while left < right:
            mid = left + (right - left) // 2

            if x < self.prefix_sums[mid]:
                right = mid
            else:
                left = mid + 1
        return left
