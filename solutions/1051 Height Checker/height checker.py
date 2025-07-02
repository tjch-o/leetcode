def height_checker(heights):
    sorted_heights = sorted(heights)
    count = 0

    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            count += 1
    return count
