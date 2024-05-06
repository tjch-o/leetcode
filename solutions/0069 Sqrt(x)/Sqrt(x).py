def my_sqrt(x):
    if x <= 1:
        return x
    else:
        square = 1

        while x >= square * square:
            square += 1
        return square - 1
