def check_powers_of_three(n):
    while n > 0:
        if n % 3 == 2:
            return False
        n = n // 3
    return True
