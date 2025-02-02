def h_index(citations):
    citations.sort(reverse=True)
    left, right = 0, len(citations)

    while left < right:
        mid = left + (right - left) // 2

        if citations[mid] >= mid + 1:
            left = mid + 1
        else:
            right = mid
    return left
