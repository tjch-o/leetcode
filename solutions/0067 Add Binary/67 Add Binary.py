def addBinary(a, b):
    def convert_binary(x): 
        if x == 0 or x == 1: 
            return str(x)
        elif x % 2 == 0: 
            return str(0) + str(convert_binary(x // 2))
        else:
            return str(1) + str(convert_binary(x // 2))
        
    # a and b are both binary strings so we convert both from base 2 to base 10 using int() 
    a_plus_b_decimal = int(a, 2) + int(b, 2)
    # 4 is "100" instead of "001" we always reverse at the end
    return convert_binary(a_plus_b_decimal)[::-1] 