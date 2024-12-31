def f(x):
    s = 0
    
    while x != 0:
        s += (x % 10) ** 2
        x = x // 10
    return s


def is_happy(n):
    seen = set()

    while n != 1:
        if f(n) == 1:
            break

        if f(n) in seen:
            return False

        n = f(n)
        seen.add(n)
    return True
