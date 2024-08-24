def maxProduct(nums):
    largest = max(nums)
    nums.remove(largest)
    secondlargest = max(nums)
    return (largest - 1) * (secondlargest - 1)