def max_area(height):
    n = len(height)
    start, end = 0, n - 1
    largest_area = float("-inf")

    while start <= end:
        lower_bound = min(height[start], height[end])
        width = end - start
        curr = lower_bound * width

        if curr > largest_area:
            largest_area = curr

        # move pointer to  potentially find a container with more height and thus more area
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return largest_area
