def find_kth_positive(arr, k):
    seen = set(arr)
    count = 0
    i = 0

    while count < k:
        i += 1

        if i not in seen:
            count += 1
    return i
