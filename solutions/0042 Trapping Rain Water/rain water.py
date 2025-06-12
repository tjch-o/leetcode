def trap(heights):
    if not heights:
        return 0

    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]
    total = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, heights[left])
            total += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            total += right_max - heights[right]
    return total
