def find_closest_elements(arr, k, x):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    closest_idx = left
    left, right = closest_idx - 1, closest_idx

    while k > 0:
        if left < 0:
            right += 1
        elif right >= len(arr):
            left -= 1
        elif abs(arr[left] - x) <= abs(arr[right] - x):
            left -= 1
        else:
            right += 1
        k -= 1
    return arr[left + 1 : right]
