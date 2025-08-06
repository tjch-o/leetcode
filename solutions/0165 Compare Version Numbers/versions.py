def append_zeros(arr, k):
    for _ in range(k):
        arr.append(0)


def compare_version(v1, v2):
    v1_arr = list(map(int, v1.split(".")))
    v2_arr = list(map(int, v2.split(".")))

    k = abs(len(v1_arr) - len(v2_arr))
    if len(v1_arr) > len(v2_arr):
        append_zeros(v2_arr, k)
    else:
        append_zeros(v1_arr, k)

    while v1_arr and v2_arr:
        x, y = v1_arr.pop(0), v2_arr.pop(0)

        if x < y:
            return -1
        elif x == y:
            continue
        else:
            return 1

    if not v1_arr and not v2_arr:
        return 0
    elif v1_arr:
        return 1
    else:
        return -1
