def delete_and_earn(nums):
    table = {}
    for number in nums:
        if number not in table:
            table[number] = nums.count(number)

    max_value = max(nums)
    points_table = [0 for _ in range(max_value + 1)]

    for i in range(1, max_value + 1):
        if i in table:
            # when we delete adjacent numbers we don't count them in the points
            current_points = i * table[i]
            # similar to the house robber problem but instead of adjacent elements we consider adjacent numbers
            points_table[i] = max(
                points_table[i - 1], points_table[i - 2] + current_points
            )

        else:
            points_table[i] = max(points_table[i - 1], points_table[i - 2])
    return points_table[max_value]
