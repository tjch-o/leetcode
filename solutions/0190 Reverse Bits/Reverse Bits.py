def reverse_bit(n):
    reversed = 0
    
    for _ in range(32):
        last_bit = n & 0x1
        exclude_last_bit = reversed << 1
        reversed = exclude_last_bit | last_bit
        n = n >> 1
    return reversed
