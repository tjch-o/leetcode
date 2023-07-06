def plusOne(digits):
    digits_mapped = list(map(lambda x: str(x), digits))
    digit_string = "".join(digits_mapped)
    digit_int = int(digit_string)

    digit_int += 1
    digit_string = str(digit_int)

    new_list = list()
    
    for digit in digit_string:
        new_list.append(int(digit))
        
    return new_list