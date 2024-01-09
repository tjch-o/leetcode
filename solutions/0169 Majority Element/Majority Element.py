def majorityElement(nums):
    # majority element is the element that appears more than n / 2 times where n is size of array
    num_d = {}
    for number in set(nums):
        num_d[number] = nums.count(number)

    highest_count = max(num_d.values())
    for number in num_d:
        if num_d[number] == highest_count:
            return number
