def count_primes(n):
    if n == 0 or n == 1:
        return 0
    
    numbers = [True for i in range(n)]
    numbers[0] = False
    numbers[1] = False
    
    for i in range(2, n):
        if numbers[i] == True:
            # all composite numbers before i * i would already have been marked False
            for j in range(i * i, n, i):
                numbers[j] = False
    
    return numbers.count(True)