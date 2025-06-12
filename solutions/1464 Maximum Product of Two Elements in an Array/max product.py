def max_product(nums):
    largest = max(nums)
    nums.remove(largest)
    second_largest = max(nums)
    return (largest - 1) * (second_largest - 1)
