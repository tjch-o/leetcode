def max_turbulence_size(arr):
    n = len(arr)
    if n == 1:
        return 1

    turbulent_end_inc, turbulent_end_dec = 1, 1
    max_l = 0

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            turbulent_end_dec = turbulent_end_inc + 1
            turbulent_end_inc = 1
        elif arr[i] > arr[i - 1]:
            turbulent_end_inc = turbulent_end_dec + 1
            turbulent_end_dec = 1
        else:
            turbulent_end_inc, turbulent_end_dec = 1, 1

        max_l = max(max_l, turbulent_end_inc, turbulent_end_dec)
    return max_l
