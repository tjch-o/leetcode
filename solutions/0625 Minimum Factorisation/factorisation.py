def smallest_factorisation(num):
    pf_digits = [i for i in range(9, 1, -1)]
    reversed_prime_factors = []

    for divisor in pf_digits:
        while num % divisor == 0:
            reversed_prime_factors.append(str(divisor))
            num = num // divisor

    if num != 1:
        return 0

    prime_factors = reversed_prime_factors[::-1]
    result = int("".join(prime_factors))
    return result if result < (2**31 - 1) else 0
