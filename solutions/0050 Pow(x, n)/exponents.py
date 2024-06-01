def my_pow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return my_pow(1 / x, -n)
    elif n % 2 == 0:
        return my_pow(x * x, n / 2)
    else:
        return x * my_pow(x, n - 1)
