def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while (left < right):
        if numbers[left] + numbers[right] == target:
            # requirement of question to add by 1 for both indexes
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1