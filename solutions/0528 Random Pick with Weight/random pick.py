import random


class Solution:
    def __init__(self, w):
        self.total = 0
        self.weights = w
        self.prefix_sums = []

        for i in range(len(self.weights)):
            self.total += self.weights[i]
            self.prefix_sums.append(self.total)

    def pickIndex(self):
        random_idx = random.randint(1, self.prefix_sums[-1])
        left, right = 0, len(self.weights) - 1

        while left < right:
            mid = (left + right) // 2

            if self.prefix_sums[mid] < random_idx:
                left = mid + 1
            else:
                right = mid
        return left
