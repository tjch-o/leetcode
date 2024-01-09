def hammingWeight(n):
    def isLastDigitOne(n):
        result = n & 1
        return result == 1
    
    def removeLastDigit(n):
        return n >> 1
    
    count = 0
    while n != 0:
        if (isLastDigitOne(n)):
            count += 1
        n = removeLastDigit(n)
    return count