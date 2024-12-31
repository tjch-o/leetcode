def multiply(num1, num2):
    def asciiConvertToNumber(s):
        return ord(s) - 48

    def rebuildNum(s):
        result = 0
        exponent = len(s) - 1
        for char in s:
            result += asciiConvertToNumber(char) * (10**exponent)
            exponent -= 1
        return result

    return str(rebuildNum(num1) * rebuildNum(num2))
