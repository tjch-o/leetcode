def intersection(nums):
    numbers = list(map(set, nums))
    result = numbers[0]

    for i in range(1, len(numbers)):
        result = result.intersection(numbers[i])

    result = list(result)
    return sorted(result)
