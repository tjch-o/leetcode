def max_area(heights):
    left, right = 0, len(heights) - 1
    largest_area = 0

    while left < right:
        width = right - left
        h = min(heights[left], heights[right])
        area = width * h

        largest_area = max(largest_area, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return largest_area
