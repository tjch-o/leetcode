def mySqrt(x):
    if x <= 1:
        return x
    else:
        square = 1
        # for 9 9 > 1 so 1 becomes 2 9 > 4 so 2 becomes 3 9 == 9 so 3 becomes 4 but with our minus it goes back to 3
        # for 8 8 > 1 so 1 becomes 2 8 > 4 so 2 becomes 3 then loop terminates but we want a 2 not a 3 since they round down
        while x >= square * square: 
            square += 1
        return square - 1   
