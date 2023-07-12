def largestNumber(nums):
    if 0 in nums and nums.count(0) == len(nums):
        return str(0)
    
    n = list(map(lambda x: str(x), nums))
    # use custom key to compare numbers with different lengths
    n.sort(key = lambda x: x * 10, reverse = True)
    return "".join(n)