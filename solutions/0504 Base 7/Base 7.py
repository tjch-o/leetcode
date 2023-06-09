def convertToBase7(num):
    if num == 0:
        return "0"
    
    isNegative = num < 0
    if isNegative:
        num = -num
        
    result = ""
    while num != 0:
        remainder = num % 7
        num = num // 7
        result += str(remainder)
    
    return result[::-1] if not isNegative else "-" + result[::-1]