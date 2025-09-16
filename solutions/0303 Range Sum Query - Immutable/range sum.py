class NumArray:

    def __init__(self, nums):
        self.prefix_sums = {}

        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            self.prefix_sums[i] = curr

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix_sums[right]
        return self.prefix_sums[right] - self.prefix_sums[left - 1]
