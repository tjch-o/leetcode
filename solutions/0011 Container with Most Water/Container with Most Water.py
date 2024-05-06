def max_area(height):
    max_area = 0
    start = 0
    end = len(height) - 1

    while start < end:
        # take the lower of the two lines
        h = min(height[start], height[end])
        width = end - start
        curr_area = h * width

        if curr_area > max_area:
            max_area = curr_area

        # move the shorter line because area is bounded by shorter line and moving it might increase the area
        if h == height[start]:
            start += 1
        else:
            end -= 1

    return max_area
